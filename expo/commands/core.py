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

import asyncio
import functools
import typing as t

from ._types import Coro, _BaseCommand
from .cog import Cog
from .context import Context

T = t.TypeVar("T")
CogT = t.TypeVar("CogT", bound="Cog")
CommandT = t.TypeVar("CommandT", bound="Command")
ContextT = t.TypeVar("ContextT", bound="Context")
P = t.ParamSpec("P")

# GroupT = t.TypeVar("GroupT", bound="Group")  # command groups.
# ErrorT = t.TypeVar("ErrorT", bound="Error")  # error event


def unwrap_function(function: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
    partial = functools.partial
    while True:
        if hasattr(function, "__wrapped__"):
            function = function.__wrapped__
        elif isinstance(function, partial):
            function = function.func
        else:
            return function


class Command(_BaseCommand, t.Generic[CogT, P, T]):
    """Represents a Prefixed Command"""

    def __new__(self, cls: t.Type[CommandT], *args: t.Any, **kwargs: t.Any) -> CommandT:
        # there is definetly a better way to do this.
        self = super().__new__(cls)
        self.__orignal_kwargs__ = kwargs.copy()
        return self

    def __init__(
        self,
        func: t.Union[
            t.Callable[t.Concatenate[CogT, ContextT, P], Coro[T]],
            t.Callable[t.Concatenate[ContextT, P], Coro[T]],
        ],
        **kwargs: t.Any
    ):
        if not asyncio.iscoroutinefunction(func):
            raise TypeError("Callback must be a asynchronous coroutine.")

        name = kwargs.get("name")
        if not isinstance(name, str):
            raise TypeError("Command name must be a string")
        self.name: str = name

        self.callback = func
        self.enabled = kwargs.get("enabled", True)
        # self.aliases = kwargs.get("aliases", [])
        # self.description = kwargs.get("description", "")

    @property
    def callback(
        self,
    ) -> t.Union[
        t.Callable[t.Concatenate[CogT, ContextT, P], Coro[T]],
        t.Callable[t.Concatenate[ContextT, P], Coro[T]],
    ]:
        return self._callback

    @callback.setter
    def callback(
        self,
        function: t.Union[
            t.Callable[t.Concatenate[CogT, ContextT, P], Coro[T]],
            t.Callable[t.Concatenate[ContextT, P], Coro[T]],
        ],
    ) -> None:
        self._callback = function
        unwrap = unwrap_function(function)
        self.module = unwrap.__module__

        try:
            ...
            # globalns = unwrap.__globals__
        except AttributeError:
            ...
            # globalns = {}
