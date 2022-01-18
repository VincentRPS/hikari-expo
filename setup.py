"""
Copyright 2021 VincentRPS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from setuptools import setup

from expo import __version__

with open("README.md") as fp:
    README = fp.read()

packages = [
    "expo",
    "expo.ui",
    "expo.api",
    "expo.ipc",
    "expo.commands",
    "expo.internal",
    "expo.lavalink",
    "expo.commands.app",
]

setup(
    name="hikari-expo",
    version=__version__,
    description="Extension module for hikari",
    long_description=README,
    long_description_content_type="text/markdown",
    author="VincentRPS",
    packages=packages,
    package_data={"expo": ["banner.txt"]},
    requires=["hikari"],
    python_requires=">=3.8.0,<3.11",
    extras_require={
        "docs": [
            "sphinx",
            "furo",
        ]
    },
    classifiers=[
        "Typing :: Typed",
        "Framework :: aiohttp",
        "Framework :: AsyncIO",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
    ],
)
