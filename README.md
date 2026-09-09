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
| UGREEN工具箱 | 2.1.0 | x86 | 0.9.27 | [LLLED_FPK](https://github.com/BearHero520/LLLED_FPK) |
| 反向代理 | 1.0.16 | 通用（x86 / ARM） | 1.1.3100 | [fnos-reverse-proxy](https://github.com/BearHero520/fnos-reverse-proxy) |

UGREEN 工具箱提供绿联 NAS 灯光控制、状态监测及兼容机型的风扇和电源管理，具体功能以机型检测结果为准。

反向代理支持 HTTP、HTTPS、WS、WSS、TCP、UDP，提供证书管理、自动签发、DDNS 和实验性系统 HTTPS 证书替换。安装前请先在飞牛应用中心安装 Node.js v22（`nodejs_v22`）。系统证书替换的实机兼容目标为 fnOS 1.2.0602，与应用基础安装版本要求不同。主包包含受限特权工作进程，无需另外安装证书部署助手；Web 和代理进程以应用用户运行，生命周期及受限工作进程需要 root。

安装包直接来自各项目的版本 Release；索引记录真实 FPK 的版本、权限、架构、大小及 SHA256。图标从同一版本安装包提取。

## 更新维护

先在原项目发布并验证目标版本，再在本仓库运行（需要 Python 3 和已登录的 GitHub CLI）：

```powershell
python scripts/refresh.py --toolbox-tag v2.1.0 --proxy-tag v1.0.16
```

脚本下载并在内存中检查 FPK，验证 GitHub SHA256、独立校验文件、大小及包内 manifest，更新 `fnpack.json` 和图标。核对变更后再提交推送；脚本不会发布原项目版本。升级时同步修改本 README 的版本表与命令。

本仓库只维护应用源索引和展示资源，原项目源码和授权条款请查看上方项目链接。FnDepot 的公开源列表由其维护者的扫描流程生成；手动添加本源无需等待该列表更新。
