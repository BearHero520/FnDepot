# BearHero 应用源

面向飞牛 fnOS 的个人应用源，遵循 [FnDepot 外部应用源 V2 规范](https://github.com/EWEDLCM/FnDepot)。

## 添加到 FnDepot

在 FnDepot 的外部应用源设置中添加此仓库地址：

```text
https://github.com/BearHero520/FnDepot
```

也可使用 JSON 直链：

```text
https://raw.githubusercontent.com/BearHero520/FnDepot/main/fnpack.json
```

使用支持 V2 外部源的 FnDepot 客户端。此源由用户自行添加，不代表 FnDepot 官方审核或推荐。

## 应用

| 应用 | 版本 | 架构 | 最低 fnOS | 项目 |
| --- | --- | --- | --- | --- |
| MiAir Plus | 2.0.9 | 通用（x86_64 / ARM64） | NAS 文件授权需 1.2.0401+ | [介绍与截图](apps/miair-plus/README.md) · [项目](https://github.com/BearHero520/miair-plus) |
| UGreen Control | 3.0.7 | x86 | 0.9.27 | [UGreen-Control](https://github.com/BearHero520/UGreen-Control) |
| 反向代理 | 1.0.18 | 通用（x86 / ARM） | 1.1.3100 | [fnos-reverse-proxy](https://github.com/BearHero520/fnos-reverse-proxy) |

UGreen Control 提供绿联 NAS 灯光控制、状态监测及兼容机型的风扇、来电恢复、WOL 和 RTC 定时开机管理。v3.0.7 修复“关于 → 项目说明”的图片路径与 Markdown 图片显示，支付宝和微信打赏码直接并排展示，点击可查看原图。应用标识仍为 `App.Native.UGreenLED`，支持覆盖升级并保留配置；实验能力与实机验证状态以应用检测和项目文档为准。详见 [v3.0.7 更新说明](https://github.com/BearHero520/UGreen-Control/releases/tag/v3.0.7)。

反向代理支持 HTTP、HTTPS、WS、WSS、TCP、UDP，提供证书管理、自动签发、DDNS 和实验性系统 HTTPS 证书替换。1.0.18 带来 iOS 18 磨砂界面、移动端适配和规则快捷启停，并修复状态标识与筛选排列，保留升级重启后的运行历史。安装前请先在飞牛应用中心安装 Node.js v22（`nodejs_v22`）。系统证书替换的实机兼容目标为 fnOS 1.2.0602，与应用基础安装版本要求不同。主包包含受限特权工作进程，无需另外安装证书部署助手；Web 和代理进程以应用用户运行，生命周期及受限工作进程需要 root。

MiAir Plus 提供小爱音箱 DLNA / AirPlay 音乐投送，以及支持上传、NAS 选曲、工作日和节假日规则的音乐闹钟。2.0.9 修复 AirPlay 音量与实时流兼容问题，新增整首播放和循环 2–20 次闹钟，优化 iOS 输入体验及投送日志；AirPlay 2 仍为预览功能，现场投送效果需安装后实测。NAS 文件授权需 fnOS 1.2.0401+ 和飞牛 App 1.34.0+，具体音箱与发送端兼容性请查看项目说明。生命周期脚本需要 root，主服务以应用用户运行。

### MiAir Plus 手机界面

<img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/dashboard.png" width="280" alt="MiAir Plus 手机总览"> <img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/alarms.png" width="280" alt="MiAir Plus 手机音乐闹钟">

[查看全部五张截图与更新说明](apps/miair-plus/README.md)

安装包直接来自各项目的版本 Release；索引记录真实 FPK 的版本、权限、架构、大小及 SHA256。图标从同一版本安装包提取。

## 更新维护

先在原项目发布并验证目标版本，再在本仓库运行（需要 Python 3 和已登录的 GitHub CLI）：

```powershell
python scripts/refresh.py --toolbox-tag v3.0.7 --proxy-tag v1.0.18
python scripts/refresh.py --miair-tag v2.0.9
```

脚本只更新指定应用并保留其他条目；MiAir 预览版需显式传入 `--allow-miair-preview`。脚本下载并在内存中检查 FPK，验证 GitHub SHA256、独立校验文件、大小及包内 manifest，更新 `fnpack.json` 和图标。核对变更后再提交推送；脚本不会发布原项目版本。升级时同步修改本 README 的版本表与命令。

应用详情页维护在 `apps/<appname>/README.md`；存在此文件时，刷新脚本会将 `readme_url` 指向本仓库详情页，保留截图展示入口。截图按应用版本存放在 `assets/screenshots/`。

本仓库只维护应用源索引和展示资源，原项目源码和授权条款请查看上方项目链接。FnDepot 的公开源列表由其维护者的扫描流程生成；手动添加本源无需等待该列表更新。

## 支持作者

如果这个应用源对你有帮助，欢迎点一颗 ⭐ **Star**，让更多人发现它。
愿意的话，也可以请作者喝杯咖啡，为应用源整理、适配测试和后续维护添一点动力。
打赏完全自愿，量力随心；你的使用、反馈和分享，同样是很好的支持。谢谢你！

| 支付宝 | 微信支付 |
| --- | --- |
| ![支付宝自愿打赏二维码](https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/donate/alipay.jpg) | ![微信支付自愿打赏二维码](https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/donate/wechat.png) |

点击图片可查看原图。
