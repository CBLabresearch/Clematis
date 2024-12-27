# Clematis

[ [中文](https://github.com/CBLabresearch/clematis/blob/main/readme_ch.md) | [English](https://github.com/CBLabresearch/clematis/blob/main/readme.md) ]

🛠️ A powerful tool for converting PE files (EXE/DLL) into position-independent shellcode.

## ✨ Key Features

- Support for converting PE files (EXE/DLL) to shellcode
- Compatible with both x86 and x64 architectures
- Command-line argument support
- Built-in LZNT1 compression algorithm for significant output file size reduction
- Optional obfuscation for enhanced stealth

## 📦 Installation

### Dependencies
```bash
pip install pefile lznt1
```

## 🚀 Usage

```bash
python clematis.py -f <PE_file> -o <output_file> [-g <true/false>] [-c <true/false>] [-p <parameters>]
```

### Parameters

- `-f, --file`: Path to the PE file to convert (required)
- `-o, --output`: Output filename (required)
- `-g, --garble`: Enable obfuscation [default: true]
- `-c, --compress`: Enable compression [default: true]
- `-p, --parameter`: Execution parameters to pass to the PE file

### Examples

```bash
# Show help information
python clematis.py -h

# Basic usage
python clematis.py -f target.exe -o output.bin

# Disable obfuscation and compression
python clematis.py -f target.exe -o output.bin -g false -c false

# Pass arguments to target program
python clematis.py -f target.exe -o output.bin -p arg1 arg2
```

---

## 🔍 How It Works

Clematis converts PE files to shellcode through the following steps:

1. Read and parse target PE file
2. Process command line arguments (if any)
3. Optional LZNT1 compression
4. Optional obfuscation processing
5. Generate final position-independent shellcode

```mermaid
flowchart TD
    A[START] --> B[Read PE file]
    B --> C[Parse PE structure]
    C --> D{Is there a command line argument?}
    D -- TRUE --> E[Process command line arguments]
    D -- FALSE --> F{Enable compression?}
    E --> F
    F -- TRUE --> G[LZNT1 compression]
    F -- FALSE --> H{Enable obfuscation?}
    G --> H
    H -- TRUE --> I[Execute obfuscation processing]
    H -- FALSE --> J[Generate shellcode]
    I --> J
    J --> K[Output result]
    K --> L[END]
```

---

## 📝 Notes

- Ensure sufficient permissions to read source PE files and write target files
- Compression is recommended when converting large files
- Obfuscation may add some performance overhead but provides better stealth

## ⚠️ Known Issues

- Parts of an application (exe) built with mingw | gcc may fail to load, it may be caused by relocation?

## 🗓️ Planned Features

- Advanced encryption options for better security
- GUI interface for easier operation
- Real-time conversion progress monitoring
- Processing of resources in PE

## 🔄 Recent Updates

- Support for .NET ( x64 | x86 )

## 🤝 Contributing

Issues and Pull Requests are welcome!
