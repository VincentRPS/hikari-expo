"""
expo
~~~~
hikari-expo is an extension module for hikari.

:copyright: 2022 VincentRPS
:license: Apache-2.0
"""

__version__: str = "1.1.0"

import typing as t

from .internal import *
from .voice import *


class VersionInfo(t.NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: t.Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=1, minor=1, micro=0, releaselevel="alpha", serial=0
)
