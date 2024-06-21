from setuptools import setup, find_packages

# 读取README.md文件的内容
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='logger_print',
    version='0.1',
    description='A simple package to redirect print statements to loguru logger.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        'Source Code': 'https://github.com/glwhappen/logger_print',
    },
    author='glwhappen',
    author_email='1597721684@qq.com',
    packages=find_packages(),
    install_requires=[
        'loguru',
    ],
)