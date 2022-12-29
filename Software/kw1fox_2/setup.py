#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

setup(
    author="Joe",
    author_email="kenwood364@gmail.com",
    python_requires=">=3.6",
    description="Software to run the KW1FOX-2 Radio Station",
    entry_points={
        "console_scripts": [
            "kw1fox_2=kw1fox_2.cli:main",
        ],
    },
    install_requires=[],
    license="BSD license",
    long_description=open("README.txt").read(),
    include_package_data=True,
    keywords="kw1fox_2",
    name="https://github.com/Kitsune-Robotics/kw1fox-2",
    packages=find_packages(include=["kw1fox_2", "kw1fox_2.*"]),
    test_suite="tests",
    url="https://github.com/kenwoodFox/kw1fox_2",
    version="0.1.0",
)
