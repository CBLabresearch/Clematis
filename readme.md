# Clematis

🛠️ 一个将 PE 文件（EXE/DLL）转换为位置无关shellcode的强大工具。

## ✨ 主要特性

- 支持将 PE 文件（EXE/DLL）转换为 shellcode
- 同时支持 x86 和 x64 架构
- 支持命令行参数传递
- 内置 LZNT1 压缩算法，显著减小输出文件大小
- 可选的混淆功能，提供更好的隐蔽性

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

- `-f, --file`: 需要转换的 PE 文件路径（必需）
- `-o, --output`: 输出文件名（必需）
- `-g, --garble`: 是否启用混淆功能 [默认: true]
- `-c, --compress`: 是否启用压缩功能 [默认: true]
- `-p, --parameter`: 传递给 PE 文件的执行参数

### 示例

```bash
# 显示帮助信息
python clematis.py -h

# 基本使用
python clematis.py -f target.exe -o output.bin

# 禁用混淆和压缩
python clematis.py -f target.exe -o output.bin -g false -c false

# 传递参数给目标程序
python clematis.py -f target.exe -o output.bin -p arg1 arg2
```

## 🔍 工作原理

Clematis 通过以下步骤将 PE 文件转换为 shellcode：

1. 读取并解析目标 PE 文件
2. 处理命令行参数（如果有）
3. 可选的 LZNT1 压缩
4. 可选的混淆处理
5. 生成最终的位置无关 shellcode

## 📝 注意事项

- 确保有足够的权限读取源 PE 文件和写入目标文件
- 建议在转换大文件时启用压缩功能
- 混淆功能可能会增加一些性能开销，但能提供更好的隐蔽性

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！
