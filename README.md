# logger_print

一行代码，即可给原有的 python 项目加上日志输出，会自动将所有的 print 函数修改为日志，并且输出到控制台和本地文件中。无需修改任何原有代码。

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
