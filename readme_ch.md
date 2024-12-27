# Clematis

[ [中文](https://github.com/CBLabresearch/clematis/blob/main/readme_ch.md) | [English](https://github.com/CBLabresearch/clematis/blob/main/readme.md) ]

🛠️ 一个强大的工具，用于将PE文件（EXE/DLL）转换为与位置无关的shellcode。

## ✨ 主要特性

- 支持将PE文件（EXE/DLL）转换为shellcode
- 同时兼容x86和x64架构
- 支持命令行参数
- 内置LZNT1压缩算法，显著减小输出文件大小
- 可选的混淆功能，增强隐蔽性

## 📦 安装

### 依赖项
```bash
pip install pefile lznt1
```

## 🚀 使用方法

```bash
python clematis.py -f <PE文件> -o <输出文件> [-g <true/false>] [-c <true/false>] [-p <参数>]
```

### 参数说明

- `-f, --file`: PE文件路径（必需）
- `-o, --output`: 输出文件名（必需）
- `-g, --garble`: 启用混淆功能 [默认: true]
- `-c, --compress`: 启用压缩功能 [默认: true]
- `-p, --parameter`: 传递给PE文件的执行参数

### 使用示例

```bash
# 显示帮助信息
python clematis.py -h

# 基本用法
python clematis.py -f target.exe -o output.bin

# 禁用混淆和压缩
python clematis.py -f target.exe -o output.bin -g false -c false

# 传递参数给目标程序
python clematis.py -f target.exe -o output.bin -p arg1 arg2
```

---

## 🔍 工作原理

Clematis通过以下步骤将PE文件转换为shellcode：

1. 读取并解析目标PE文件
2. 处理命令行参数（如果有）
3. 可选的LZNT1压缩
4. 可选的混淆处理
5. 生成最终的位置无关shellcode

```mermaid
flowchart TD
    A[开始] --> B[读取PE文件]
    B --> C[解析PE结构]
    C --> D{是否有命令行参数?}
    D -- 是 --> E[处理命令行参数]
    D -- 否 --> F{是否启用压缩?}
    E --> F
    F -- 是 --> G[LZNT1压缩]
    F -- 否 --> H{是否启用混淆?}
    G --> H
    H -- 是 --> I[执行混淆处理]
    H -- 否 --> J[生成shellcode]
    I --> J
    J --> K[输出结果]
    K --> L[结束]
```

---

## 💪 我们的优势

- 🎯 支持 DOT NET
- 🗜️ 支持压缩
- 🎭 支持混淆
- 🔄 支持参数传递
- 🚀 对golang进行完全的支持
- 💪 构造的shellcode非常的强大且稳定

## 💡 设计理念

##### 在某些特殊环境中，我们可能会遇到以下挑战：

```text
- 🛡️ 无法进行进程注入（AV/EDR/XDR拦截）
- 🔄 当前进程中执行golang程序可能导致阻塞
- 💾 golang程序执行后可能存在内存泄漏
- ⚠️ golang创建的线程无法释放！
```

##### 为解决这些问题，我们开发了clematis：

```
- ✨ 将golang程序转换为shellcode
- 🎯 在当前进程中直接执行
- ♻️ 执行完毕后自动释放内存
- 🚀 完全避免golang相关的内存问题
- 🔄 回收golang创建的所有线程
```

## 📝 注意事项

- 确保有足够的权限读取源PE文件和写入目标文件
- 转换大文件时建议启用压缩功能
- 混淆可能会增加一些性能开销，但能提供更好的隐蔽性

## ⚠️ 已知问题

- 使用mingw | gcc编译的应用程序（exe）的部分内容可能无法加载，这可能是由重定位导致的？

## 🗓️ 计划功能

- 更高级的加密选项以提升安全性
- 图形界面支持，便于操作
- 实时转换进度监控
- 处理PE中的资源

## 🔄 最近更新

- 支持 DOT NET（x64 | x86）

## 🤝 贡献

欢迎提交Issues和Pull Requests！
