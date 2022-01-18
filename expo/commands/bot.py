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
# An instance of hikari.GatewayBot with a built in command handler.
import concurrent
import typing

import hikari
from hikari import Intents, config

from .core import Command


# for anyone running mypy, there is a lot of errors here...
# i am too lazy to fix them so i will just ignore it,
# if you find whats wrong you can just make a PR!
class Bot(hikari.GatewayBot):
    def __init__(
        self,
        token: str,
        *,
        command_prefix: str = ...,
        allow_color: bool = True,
        banner: typing.Optional[str] = "hikari",
        executor: typing.Optional[concurrent.futures.Executor] = None,
        force_color: bool = False,
        cache_settings: typing.Optional[config.CacheSettings] = None,
        http_settings: typing.Optional[config.HTTPSettings] = None,
        intents: Intents = ...,
        logs: typing.Union[None, int, str, typing.Dict[str, typing.Any]] = "INFO",
        max_rate_limit: float = 300,
        max_retries: int = 3,
        proxy_settings: typing.Optional[config.ProxySettings] = None,
        rest_url: typing.Optional[str] = None
    ) -> None:
        self.command_prefix = command_prefix
        super().__init__(
            token,
            banner,
            executor,
            force_color,
            cache_settings,
            http_settings,
            intents,
            logs,
            max_rate_limit,
            max_retries,
            proxy_settings,
            rest_url,
            allow_color=allow_color,
        )

    def command(self) -> Command:
        return Command
