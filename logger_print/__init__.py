import sys

from loguru import logger
# 移除 loguru 默认添加的所有处理器
logger.remove()

custom_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{file}</cyan>:<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.level("PRINT", no=21, color="<black>")
# 添加控制台输出，使用控制台格式
# logger.add(sys.stderr, format=custom_format)
# 添加文件输出，使用文件格式
logger.add("logger_print.log", format=custom_format, rotation="1 week")

console_format = "<green>{file}:{function}:{line}</green> | <level>{message}</level>"

# 添加控制台输出，使用控制台格式
logger.add(sys.stderr, format=console_format, enqueue=False)

def print(*args, **kwargs):
    log_message = " ".join(str(arg) for arg in args)
    if 'sep' in kwargs:
        log_message = kwargs.get('sep', ' ').join(str(arg) for arg in args)
    logger.opt(depth=1).log("PRINT", log_message)

if __name__ == '__main__':
    print("你好", "哈哈哈")
    print("你好")