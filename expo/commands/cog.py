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
# heavily inspired by discord.py's Cog system.
import inspect
import typing as t

from ._types import _BaseCommand
from .core import Command

FuncT = t.TypeVar("FuncT", bound=t.Callable[..., t.Any])


class CogMeta(type):
    """A meta class for defining a expo Cog

    .. note::

        This isn't recommened you use this class as a base for Cog's
        as it doesn't actually have the Cog impl.
    """

    __cog_name__: str
    __cog_settings__: t.Dict[str, t.Any]
    __cog_commands__: t.List[Command]
    __cog_listeners__: t.List[t.Tuple[str, str]]

    def __new__(  # noqa: ignore
        self, cls: t.Type["CogMeta"], *args: t.Any, **kwargs: t.Any
    ) -> "CogMeta":
        name, bases, attrs = args
        attrs["__cog_name__"] = kwargs.pop("name", name)
        attrs["__cog_settings"] = kwargs.pop("command_attrs", {})

        description = kwargs.pop("description")
        if description is None:
            description = inspect.cleandoc(attrs.get("__doc__"), "")
        attrs["__cog_description"] = description

        commands = {}
        listeners = {}

        new_cls = super().__new__(cls, name, bases, attrs, **kwargs)
        for base in reversed(new_cls.__mro__):
            for elem, value in base.__dict__.items():
                if elem in commands:
                    del commands[elem]
                elif elem in listeners:
                    del listeners[elem]

                is_static_method = isinstance(value, staticmethod)
                if is_static_method:
                    value = value.__func__
                if isinstance(value, _BaseCommand):
                    if is_static_method:
                        raise TypeError(
                            f"The certain command in {base}.{elem!r} can't be a static method."
                        )
                    if elem.startswith(("bot_", "cog_")):
                        raise TypeError(
                            f"{elem} is not allowed to have `bot_` or `cog_` in the name."
                        )

                    commands[elem] = value
                elif inspect.iscoroutinefunction(value):
                    try:
                        getattr(value, "__cog_listener__")
                    except AttributeError:
                        continue
                    else:
                        if elem.startswith(("bot_", "cog_")):
                            raise TypeError(
                                f"{elem} is not allowed to have `bot_` or `cog_` in the name."
                            )
                        listeners[elem] = value

        new_cls.__cog_commands__ = list(commands.values())

        listeners_list = []
        for listener in listeners.values():
            for listener_name in listeners.__cog_listener_names:
                listeners_list.append(listener_name, listener.__name__)

        new_cls.__cog_listeners__ = listeners_list
        return new_cls

    def __init__(self, *args: t.Any, **kwargs: t.Any):
        super().__init__(*args)

    @classmethod
    def qualified_name(cls) -> str:
        return cls.__cog_name__


def cog_method(func: FuncT) -> FuncT:
    func.__cog_special_method__ = None
    return func


class Cog(metaclass=CogMeta):
    """The base Cog class for expo which every Cog inherits from."""

    __cog_name__: str
    __cog_settings__: t.Dict[str, t.Any]
    __cog_commands__: t.List[Command]
    __cog_listeners__: t.List[t.Tuple[str, str]]

    ...
