import typing as t

from .voice import *
from .internal import *

class VersionInfo(t.NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: t.Literal["alpha", "beta", "candidate", "final"]
    serial: int

version_info: VersionInfo
