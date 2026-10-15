# 许可与出处核对：2026-10-15

核对范围为之前测试选用的五个公开包。这里记录公开仓库元数据、固定版本与代码来源判断，不保存本地路径、账户数据、运行日志或第三方实现。

| 先前内部测试包 | 原始发布/取得位置 | 本仓库处理 |
| --- | --- | --- |
| client_eprendre | [hanzj 固定 commit 备份](https://github.com/hanzj/hanzj.github.io/tree/6c4841eb5b95c15a94f377914a2f643d5c0c88a2/images/2025)，原项目 [eprendre/tingshu](https://github.com/eprendre/tingshu) | 只引用固定备份原 JAR URL；不复制测试裁剪包或宿主代码 |
| client_free12 | [freefly22 固定 commit](https://github.com/freefly22/tingshu-free-jar/tree/74e7762a07ffbcac09e207fa2833ff7ee43c915a) | 只引用原 free_all_v12.jar URL |
| client_m1ngzer | [m1ngzer 固定 commit](https://github.com/m1ngzer/tingshu-sources/tree/5902a600be4b83165a7bdc3340d37b3a400d65ed) | 只引用原 sources_by_m1ngzer.jar URL |
| client_sound | [wsl201 固定 commit 备份](https://github.com/wsl201/ts/tree/59b6d19121e86fa01a95aab5876773fae9afc711/jar) | 只引用原 my_sound_01.jar URL |
| client_shun | 同一 wsl201 固定备份 | 只引用原 sources_by_shun.jar URL |

原包散列已从先前固定下载记录核对，见根目录 `UPSTREAM-SHA256SUMS`。这些散列描述原输入，不是经过裁剪或修改后的二进制。

GitHub 官方 repository metadata 当前对 eprendre、freefly22、m1ngzer、hanzj、wsl201 及交叉备份 zihao-wangx / dupontjoy88 均返回 `license:null`，对应 license endpoint 为 404；公开字段记录见本目录两个 license-metadata JSON。已缓存完整树未见 LICENSE/COPYING/NOTICE，相关 README 未见明确再分发授权。公开源码或下载说明不能代替明确许可。备份仓库也不能证明其对原作者代码取得了再授权权利。

因此没有可标记为已许可、可嵌入本仓库发布的第三方包。没有生成包含五包/15项源的 qingting_sources 聚合 JAR，没有复制 SDK、反编译专有类或原 APK。当前交付使用正常源管理认可的标准 JSON，把下载交给已经存在的固定上游地址。

五条原包 HTTPS 地址的 HEAD 均成功（仅 URL 可达性；不下载二进制，不验证作者签名），详见 `upstream-url-checks.json`。源管理/播放样本验证与许可是两个不同事实；测试范围见 `upstream-catalog.json`，不把可播放等同于已获再分发许可。

原生 RSS/LibriVox 新适配器未在本轮实现或宣称可用；它需要独立内容/API与宿主验证，不用“空源包”代替实际可导入目录。
