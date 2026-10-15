#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build normal TingShu subscription metadata without mirroring third-party code."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request


def repository_default():
    parent = Path(__file__).resolve().parents[1]
    return parent if (parent / 'upstream-catalog.json').is_file() else parent / 'source-repository'


def checked_package(row):
    assert re.fullmatch(r'[a-z0-9_]+', row['id']), 'Invalid catalog identity'
    assert re.fullmatch(r'[A-Za-z0-9_]+', row['entry_package']), 'Invalid entry package'
    assert type(row['version']) is int and 0 <= row['version'] <= 2147483647
    assert re.fullmatch(r'[a-f0-9]{40}', row['commit']), 'Unpinned upstream commit'
    assert re.fullmatch(r'[a-f0-9]{64}', row['sha256']), 'Missing upstream hash'
    repo = urllib.parse.urlparse(row['repository_url'])
    assert repo.scheme == 'https' and repo.netloc == 'github.com'
    assert re.fullmatch(r'/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo.path)
    expected = 'https://raw.githubusercontent.com' + repo.path + '/' + row['commit'] + '/'
    assert row['download_url'].startswith(expected), 'Download must stay on its pinned upstream'
    assert row['download_url'].endswith('.jar') and '..' not in row['download_url'].split('/')
    assert row['subscription_file'] == 'subscriptions/' + row['id'] + '.json'
    return row


def subscription(row):
    kind = '作者/发布者仓库' if row['distribution_kind'] == 'publisher_repository' else '社区备份'
    return {
        'version': row['version'],
        'entry_package': row['entry_package'],
        'download_url': row['download_url'],
        'update_msg': kind + '原包链接；本目录不镜像或修改二进制。请在源管理中自行勾选。',
        'support_url': row['repository_url'],
        'desc': kind + '；明确再分发许可尚未确认',
    }


def head(row):
    result = {'id': row['id'], 'url': row['download_url'], 'expected_sha256': row['sha256'],
              'hash_check': 'Previously pinned local artifact; HEAD does not rehash bytes.'}
    try:
        request = urllib.request.Request(row['download_url'], method='HEAD',
                                         headers={'User-Agent': 'TingShuSourceMetadataCheck/1'})
        with urllib.request.urlopen(request, timeout=20) as response:
            result.update(http_status=response.status,
                          content_length=response.headers.get('Content-Length'),
                          final_host=urllib.parse.urlparse(response.url).hostname)
        result['passed'] = result['http_status'] == 200 and result['final_host'] == 'raw.githubusercontent.com'
    except urllib.error.HTTPError as error:
        result.update(http_status=error.code, passed=False)
    except Exception as error:
        result.update(error=type(error).__name__, passed=False)
    return result


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-dir', type=Path, default=repository_default())
    parser.add_argument('--verify-upstreams', action='store_true', help='HEAD fixed public upstream URLs; no JAR download')
    parser.add_argument('--bundle', action='store_true', help='Check whether binary aggregation is permitted (currently unavailable)')
    args = parser.parse_args()
    repo = args.repo_dir.resolve()
    catalog = json.loads((repo / 'upstream-catalog.json').read_text(encoding='utf-8'))
    assert catalog['schema'] == 1 and catalog['distribution_mode'] == 'metadata_only_upstream_urls'
    rows = [checked_package(row) for row in catalog['packages']]
    assert len({row['id'] for row in rows}) == len(rows)
    by_id = {row['id']: row for row in rows}
    assert catalog['default_subscription'] in by_id
    if args.bundle:
        refused = [row['id'] for row in rows if not row.get('redistribution_allowed')]
        parser.error('No aggregate JAR is built: no verified redistribution grants for '
                     + ', '.join(refused) + '. Use the working upstream subscription metadata.')
    for row in rows:
        write_json(repo / row['subscription_file'], subscription(row))
    write_json(repo / 'external_sources.json', subscription(by_id[catalog['default_subscription']]))
    # A clone of this staging repository can regenerate its metadata without this workspace.
    script_copy = repo / 'tools/build_external_sources.py'
    script_copy.parent.mkdir(exist_ok=True)
    if script_copy.resolve() != Path(__file__).resolve():
        shutil.copyfile(__file__, script_copy)
    checks = None
    if args.verify_upstreams:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            checks = list(pool.map(head, rows))
        write_json(repo / 'audit/upstream-url-checks.json', {'checks': checks, 'binary_downloaded': False})
    (repo / 'UPSTREAM-SHA256SUMS').write_text(
        '# Expected hashes of pinned upstream JARs, not binaries hosted by this repository.\n'
        + ''.join(row['sha256'] + '  ' + row['download_url'] + '\n' for row in rows), encoding='utf-8')
    files = [path for path in repo.rglob('*') if path.is_file()
             and not set(path.relative_to(repo).parts) & {'.build', '__pycache__', '.git'}
             and path.name != 'SHA256SUMS' and path.suffix not in {'.pyc', '.jar', '.apk', '.class', '.dex'}]
    (repo / 'SHA256SUMS').write_text(''.join(
        hashlib.sha256(path.read_bytes()).hexdigest() + '  ' + path.relative_to(repo).as_posix() + '\n'
        for path in sorted(files)), encoding='utf-8')
    print(json.dumps({'subscriptions': len(rows), 'default_entry': by_id[catalog['default_subscription']]['entry_package'],
                      'binary_files_generated': 0,
                      'upstream_heads_passed': None if checks is None else sum(row['passed'] for row in checks)}, ensure_ascii=True))
    if checks is not None and not all(row['passed'] for row in checks):
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
