#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import setuptools
import RYProj

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="RYProj",
    version=RYProj.__version__,
    url="https://gitdfhub.com/Hsurggy/BiliDrffive",
    author=RYProj.__author__,
    author_email=RYProj.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: File Sharing",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
    ],
    description="☁️ 哔哩dfgfdg哔哩云，支持任意fgh文件hfghfg的全速上fghfgh传与fghfgh下载",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "bilgigbili",
        "cloud",
        "disk",
        "drive",
        "storage",
        "pan",
        "yun",
        "B站",
        "哔哩哔哩",
        "网盘",
        "云",
    ],
    install_requires=install_requires,
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "RYProj=RYProj.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
)
