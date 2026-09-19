# MiAir Plus 2.0.9

为小爱音箱扩展 DLNA / AirPlay 音乐投送与自定义音乐闹钟，支持飞牛 fnOS 原生安装。

[下载安装包](https://github.com/BearHero520/miair-plus/releases/tag/v2.0.9) · [项目源码](https://github.com/BearHero520/miair-plus) · [问题反馈](https://github.com/BearHero520/miair-plus/issues)

## 新版优化

- **AirPlay 投送**：音量请求移到后台，避免慢云响应阻塞音频接收；修复最低音量误静音、音箱音量未同步及实时流 Range 探测兼容问题。
- **音乐闹钟**：支持完整播放一首、整首循环 2–20 次和按时长播放；新建默认整首，旧闹钟保留原设置，编辑后可切换模式。
- **iOS 输入**：调整移动端输入字号，避免输入时自动放大，保留手动缩放。
- **故障排查**：新增接收、转码和音箱拉流日志，便于定位投送故障。

## 主要功能

- 小米账号扫码登录、音箱管理、自定义投送名称，支持 DLNA 和传统 AirPlay 音频投送。
- 从电脑或手机上传音乐，或从 NAS 选择并授权文件；导入后可在铃声库复用。
- 自定义闹钟时间、目标音箱、音量与播放时长，支持指定星期、法定工作日（含调休补班）、休息日和节假日规则。
- 内置 FFmpeg，提供深浅色外观、服务状态及脱敏诊断日志。

## 安装与升级

下载 `miair-plus-2.0.9-all.fpk`，在飞牛应用中心使用“手动安装”安装或升级。x86_64 / ARM64 共用此包，不支持 ARM32；无需另装 Docker、Python 或 Node.js。

升级后关闭旧页面，从应用中心重新打开，以使用新的网关入口和权限声明。NAS 文件授权需 **fnOS 1.2.0401+、飞牛 App 1.34.0+**，并从飞牛应用入口访问；独立端口访问可使用上传音乐。

远程入口用于管理页面，DLNA / AirPlay 发现与投送仍需满足局域网条件。闹钟需要 NAS 与音箱在线，独立于小爱自带闹钟。

2.0.9 已通过自动测试、模拟音频链路验证，以及 Go、前端、双架构构建与安装脚本检查；AirPlay 是否解决现场无声仍需安装后实测，其他音箱与发送端需分别验证。**AirPlay 2 仍为预览功能**，不支持屏幕镜像、视频接收，不保证多房间精确同步。详见[兼容说明](https://github.com/BearHero520/miair-plus/blob/main/docs/COMPATIBILITY.md)。

## 手机实机截图

以下保留 2.0.5 在手机飞牛 App 中的实机截图，2.0.9 的新增功能与界面以实际安装为准。

### 总览

<img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/dashboard.png" width="360" alt="手机总览：投送服务、音箱和账号状态">

### 音箱管理

<img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/devices.png" width="360" alt="手机音箱管理：投送名称与兼容模式">

### 音乐闹钟

<img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/alarms.png" width="360" alt="手机闹钟：工作日规则、音乐与响铃日期">

### 偏好设置

<img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/settings.png" width="360" alt="手机设置：AirPlay 开关及内置 FFmpeg 状态">

### 关于

<img src="https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/screenshots/miair-plus/2.0.5/about.png" width="360" alt="关于页面：2.0.5 正式版及项目链接">

## 来源与许可

项目使用 GPL-3.0，基于 miair-next 开发线继续改造，并参考 MiAir。感谢上游作者及相关开源组件贡献；详见[来源与许可](https://github.com/BearHero520/miair-plus/blob/main/UPSTREAM.md)。
