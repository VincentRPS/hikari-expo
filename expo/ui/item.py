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
# This file is mostly based off the discord.py impl.
from __future__ import annotations

import typing as t

# from .interaction import Interaction

if t.TYPE_CHECKING:
    from .view import View

V = t.TypeVar("V", bound="View", covariant=True)


class Item(t.Generic[V]):
    """The base class for any component."""

    ...
