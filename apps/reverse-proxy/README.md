# 反向代理 1.0.18

面向飞牛 fnOS 的原生多协议反向代理应用，支持桌面端和移动端。

[下载安装包](https://github.com/BearHero520/fnos-reverse-proxy/releases/tag/v1.0.18) · [项目源码](https://github.com/BearHero520/fnos-reverse-proxy) · [问题反馈](https://github.com/BearHero520/fnos-reverse-proxy/issues)

## 主要功能

- HTTP、HTTPS、WebSocket、WSS、TCP 和 UDP 协议
- 离散端口与连续端口范围映射
- 规则新增、编辑、复制、启停、删除、搜索和筛选
- PEM、CRT、CER、KEY、DER、PFX、P12 证书导入与自动解析
- Cloudflare、阿里云 DNS 和腾讯云 DNSPod DDNS
- Let’s Encrypt、阿里云免费证书申请与临期轮换
- 实验性系统 HTTPS 证书替换，支持预检、备份、验证和失败回退
- Webhook 通知、局域网目标发现、配置导入导出和诊断包

## 更新历史

| 版本 | 日期 | 主要更新 |
| --- | --- | --- |
| [1.0.18](https://github.com/BearHero520/fnos-reverse-proxy/releases/tag/v1.0.18) | 2026-09-23 | 修复规则状态标识留白，集中状态筛选，升级重启保留运行历史。 |
| [1.0.16](https://github.com/BearHero520/fnos-reverse-proxy/releases/tag/v1.0.16) | 2026-09-09 | 增加证书自动签发与轮换、DDNS、规则内证书选择和实验性系统 HTTPS 替换。 |
| [1.0.4](https://github.com/BearHero520/fnos-reverse-proxy/releases/tag/v1.0.4) | 2026-09-04 | 完成原生 fnOS 安装包和多协议代理能力。 |
| [1.0.3](https://github.com/BearHero520/fnos-reverse-proxy/releases/tag/v1.0.3) | 2026-09-04 | 初始公开版本。 |

完整的版本、安装包大小和 SHA256 已同步到源索引的 `releases` 字段。

## 安装要求

- fnOS 1.1.3100 或更高版本
- x86 或 ARM 平台
- 安装前先在飞牛应用中心安装 Node.js v22，包名为 `nodejs_v22`

系统 HTTPS 证书替换的实机兼容目标为 fnOS 1.2.0602。Web 和代理进程以应用用户运行，生命周期及受限证书工作进程需要 root。

项目版权与授权信息以[项目仓库](https://github.com/BearHero520/fnos-reverse-proxy/tree/v1.0.18)为准。
