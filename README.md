# logger_print

`logger_print` 是一个 Python 包，用于替代标准的 `print` 函数，将输出重定向到 `loguru` 日志系统，提供了更丰富的日志功能，包括日志级别控制、彩色输出、以及异步日志记录等。

## 安装

您可以通过 pip 安装 `logger_print`:

```bash
pip install logger_print
```

## 快速开始

在任何现有的项目中，直接引入 `from logger_print import print` 即可

```python
from logger_print import print

# 使用 print，现在它会通过 loguru 输出日志
print("Hello, logger_print!")
```
