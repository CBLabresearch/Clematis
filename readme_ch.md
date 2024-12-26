# Clematis

[ [中文](https://github.com/CBLabresearch/clematis/blob/main/readme_ch.md) | [English](https://github.com/CBLabresearch/clematis/blob/main/readme.md) ]

🛠️ 一个强大的工具，用于将PE文件（EXE/DLL）转换为位置无关的shellcode。

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

## 🔍 工作原理

Clematis通过以下步骤将PE文件转换为shellcode：

1. 读取并解析目标PE文件
2. 处理命令行参数（如果有）
3. 可选的LZNT1压缩
4. 可选的混淆处理
5. 生成最终的位置无关shellcode

## 📝 注意事项

- 确保有足够的权限读取源PE文件和写入目标文件
- 转换大文件时建议启用压缩功能
- 混淆可能会增加一些性能开销，但能提供更好的隐蔽性

## 🤝 贡献

欢迎提交Issues和Pull Requests！
