# 听书订阅目录

面向“我的听书”兼容宿主的普通外置源订阅。这里只托管订阅 JSON，下载地址指向公开上游的固定原包；不镜像、不修改 JAR，不内置广告屏蔽、自动勾选或应用业务代码。许可证只覆盖本仓库自己的代码与说明，详见 [NOTICE](NOTICE.md)。

以下 `Analulua/tingshu-sources` 订阅地址可复制使用。

## 添加方式

1. 打开应用 → 听书源（旧界面叫“源管理”）→ 点击“添加订阅”卡片的加号；旧界面使用右上角“添加”。
2. 粘贴下面一个 **JSON 订阅地址**，确认并等待下载完成。
3. 进入新增源组，手动勾选要使用的源；再回“源”页面选择或正常搜索。

订阅元数据不是音频地址。若提示“源已存在”，在原源管理中更新或先确认删除的是对应测试组，不要清除整个应用数据。仓库不会自动加入到应用，也不会替用户勾选所有源。

清新版安装包首次安装只提供本地/网盘/局域网功能，网络源由用户自行添加；添加、勾选、更新、删除均在应用内完成，无需 ADB。请复制并粘贴完整订阅地址，避免输入法自动改写 URL。

## 默认订阅：eprendre 社区备份

```text
https://raw.githubusercontent.com/Analulua/tingshu-sources/main/external_sources.json
```

该 JSON 使用原标准 `version / entry_package / download_url` 字段，指向 hanzj 仓库固定 commit 的 `sources_by_eprendre.jar`。它是 **社区备份，非作者授权发布证明**。本地正常源管理曾显示 14 项；博看公开章节已验证播放。没有验证包内每个源、所有书籍或付费章节，也不声称存在 19 项全部可用。

原备份订阅地址也可直接添加，其 JSON 内下载地址由该上游维护：

```text
https://raw.githubusercontent.com/hanzj/hanzj.github.io/6c4841eb5b95c15a94f377914a2f643d5c0c88a2/images/2025/external_sources.json
```

## 作者/发布者仓库

这里的“发布者”表示原仓库提供该插件/源码，不代表已获得全部引用代码或平台内容的授权。本目录仍未找到明确二进制再分发许可，故只指向上游原包。

| 本目录订阅地址 | 上游 | 已验证子集与范围 |
| --- | --- | --- |
| `https://raw.githubusercontent.com/Analulua/tingshu-sources/main/subscriptions/freefly.json` | [freefly22/tingshu-free-jar](https://github.com/freefly22/tingshu-free-jar) | 喜马拉雅、酷我音乐、悦听吧的匿名短样本；全包含其他源，未全部验证 |
| `https://raw.githubusercontent.com/Analulua/tingshu-sources/main/subscriptions/m1ngzer.json` | [m1ngzer/tingshu-sources](https://github.com/m1ngzer/tingshu-sources) | 书音FM、听友听书的匿名短样本 |

作者原订阅（会由原作者维护，与本目录固定原包版本不同）：

```text
https://raw.githubusercontent.com/freefly22/tingshu-free-jar/main/source.json
https://m1ngzer.github.io/tingshu-sources/external_sources.json
```

## 其他社区备份

| 本目录订阅地址 | 上游 | 已验证子集与范围 |
| --- | --- | --- |
| `https://raw.githubusercontent.com/Analulua/tingshu-sources/main/subscriptions/eprendre.json` | [hanzj/hanzj.github.io](https://github.com/hanzj/hanzj.github.io) | 同默认订阅 |
| `https://raw.githubusercontent.com/Analulua/tingshu-sources/main/subscriptions/sound.json` | [wsl201/ts](https://github.com/wsl201/ts) | 仅米听书短样本；原包其他源未覆盖 |
| `https://raw.githubusercontent.com/Analulua/tingshu-sources/main/subscriptions/shun.json` | [wsl201/ts](https://github.com/wsl201/ts) | 仅有听网短样本；原包其他源未覆盖 |

前期 15 项验证针对特定选择子集及当时测试宿主，不等于这五个完整原包已经在所有版本宿主回归。新宿主对每个原包仍应按正常添加 → 勾选 → 搜索/分类 → 免费章节验证；遇到登录、验证码、付费内容时使用正常平台流程。本目录未复制原应用的“中华听书网”类或其他反编译专有实现，也未发布该第 16 源。

## 维护与校验

```text
python tools/build_external_sources.py
python tools/build_external_sources.py --verify-upstreams
```

第一条由 `upstream-catalog.json` 生成标准订阅与校验清单；第二条只 HEAD 检查固定 HTTPS 原包地址，不下载/保存 JAR、不绕过 TLS。`SHA256SUMS` 校验本仓库文本，`UPSTREAM-SHA256SUMS` 记录此前核对的固定上游原包散列；HEAD 不等于重新验证散列。

`--bundle` 当前明确拒绝：没有经过许可确认的可嵌入第三方代码，因此不会把 15 源聚合成看似可发布的新 JAR。当前可实际使用的交付是普通订阅元数据和原宿主的手动源管理。
