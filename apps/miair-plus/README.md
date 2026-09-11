# MiAir Plus 2.0.5

为小爱音箱扩展 DLNA / AirPlay 音乐投送与自定义音乐闹钟，支持飞牛 fnOS 原生安装。

[下载安装包](https://github.com/BearHero520/miair-plus/releases/tag/v2.0.5) · [项目源码](https://github.com/BearHero520/miair-plus) · [问题反馈](https://github.com/BearHero520/miair-plus/issues)

## 新版优化

- **飞牛远程入口**：通过统一网关复用飞牛系统域名与 HTTPS，保留局域网 8310 直接访问。修复入口和资源路径造成的页面加载问题。
- **手机操作**：底部导航提供总览、音箱、闹钟、设置、更多；账号、日志和关于位于“更多”。适配底部安全区域及 WebView 存储兼容，电脑端继续使用侧栏。
- **登录与数据加载**：修复飞牛网关与应用令牌冲突、移动端来源校验误拒绝，以及音箱、闹钟列表加载异常。
- **NAS 选曲**：完善原生文件选择器、文件权限校验、授权回调与错误提示，避免取消后旧结果写入新表单。
- **组件状态**：修复设置未加载成功时误报 FFmpeg 不可用的问题，接口与页面加载失败时提供明确提示。

## 主要功能

- 小米账号扫码登录、音箱管理、自定义投送名称，支持 DLNA 和传统 AirPlay 音频投送。
- 从电脑或手机上传音乐，或从 NAS 选择并授权文件；导入后可在铃声库复用。
- 自定义闹钟时间、目标音箱、音量与播放时长，支持指定星期、法定工作日（含调休补班）、休息日和节假日规则。
- 内置 FFmpeg，提供深浅色外观、服务状态及脱敏诊断日志。

## 安装与升级

下载 `miair-plus-2.0.5-all.fpk`，在飞牛应用中心使用“手动安装”安装或升级。x86_64 / ARM64 共用此包，不支持 ARM32；无需另装 Docker、Python 或 Node.js。

升级后关闭旧页面，从应用中心重新打开，以使用新的网关入口和权限声明。NAS 文件授权需 **fnOS 1.2.0401+、飞牛 App 1.34.0+**，并从飞牛应用入口访问；独立端口访问可使用上传音乐。

远程入口用于管理页面，DLNA / AirPlay 发现与投送仍需满足局域网条件。闹钟需要 NAS 与音箱在线，独立于小爱自带闹钟。

2.0.5 已收到当前设备和环境下实测正常的反馈，其他音箱与发送端需分别验证。**AirPlay 2 仍为预览功能**，不支持屏幕镜像、视频接收，不保证多房间精确同步。详见[兼容说明](https://github.com/BearHero520/miair-plus/blob/main/docs/COMPATIBILITY.md)。

## 手机实机截图

以下为 2.0.5 在手机飞牛 App 中的界面。

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
