import typing as t

T = t.TypeVar("T")
Coro = t.Coroutine[t.Any, t.Any, T]


class _BaseCommand:
    __slots__ = ()
