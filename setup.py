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
    author=RYProj.__author__,
    author_email=RYProj.__email__,
    description="☁️ fsdfs上传与fd下载",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://githhhub.com/Hhgsury/RYPghroj",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "RYProj=RYProj.__main__:main",
        ],
    }
)
