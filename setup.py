from setuptools import setup, find_packages

setup(
    name="math_quiz",                     # 项目名称
    version="0.1.0",                      # 项目版本
    description="A simple math quiz tool", # 项目简介
    long_description=open("README.md").read(),  # 详细描述（通常来自 README.md）
    author="HBen",                   # 作者
    author_email="zylalala666@163.com",# 作者邮箱
    url="https://github.com/JOKER-3-z/FAU_dsss_homework_2-", # 项目主页地址
    packages=find_packages(),             # 自动发现所有 Python 包
    install_requires=[
    ],
    python_requires='>=3.7',              # 指定 Python 版本
)
