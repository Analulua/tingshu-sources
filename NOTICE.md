# 第三方来源与许可范围

本仓库只发布自己的订阅元数据、说明和生成脚本，不存储第三方 JAR、APK、反编译源码、音频、账号或密钥。

公开可下载不代表获得开源或二进制再分发许可。2026-10-15 核对下列仓库的 GitHub 官方 license 元数据与已有文件树，未找到明确 LICENSE/COPYING/NOTICE 或 README 再分发授权，官方 `/license` 接口均为 404。`license:null` 仅描述 GitHub 检测结果；它不是版权已消失或作者无法另行授权的结论。

- 原宿主/公开 SDK 项目：[eprendre/tingshu](https://github.com/eprendre/tingshu)。本仓库不复制其 SDK 或应用实现。
- 作者/发布者仓库：[freefly22/tingshu-free-jar](https://github.com/freefly22/tingshu-free-jar)、[m1ngzer/tingshu-sources](https://github.com/m1ngzer/tingshu-sources)。存在公开源码或编译包，但未找到明确再分发授权。
- 本目录实际使用的社区备份：[hanzj/hanzj.github.io](https://github.com/hanzj/hanzj.github.io)、[wsl201/ts](https://github.com/wsl201/ts)。备份不是作者签发或授权证明。
- 交叉核对的相同二进制备份：[zihao-wangx/tingshu-backup](https://github.com/zihao-wangx/tingshu-backup)、[dupontjoy88/Tingshu-Source](https://github.com/dupontjoy88/Tingshu-Source)。本目录不从它们重新分发二进制。

本目录引用固定上游 commit 的原包地址，未改写二进制。预期原包散列见 `UPSTREAM-SHA256SUMS`，出处与短样本验证范围见 `upstream-catalog.json`。散列只帮助识别已核对内容，不证明作者签名、内容版权或所有功能安全可用。

现有五包的明确再分发许可均尚未确认，因此这里不发布把它们嵌入的 `qingting_sources.jar`，也不把源码展示、备份或下载链接当作许可授予。若未来取得许可，须另外保留相应版权声明，并满足通知、源码或其他附带条件，再评估独立源包；当前脚本 `--bundle` 会明确拒绝，不会生成“空源成功”包。

正常使用仍遵循上游平台的登录、验证码、免费/付费边界。本目录不提供登录凭据，不解除付费限制，也不承诺某个站点持续可用。

