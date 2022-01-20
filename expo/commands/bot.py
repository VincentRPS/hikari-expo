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
import typing as t

import hikari

from .core import Command


def on_mention(bot: "Bot", spaced: bool = False):
    me = bot.get_me()
    mentions = (
        [f"<@{me.id}> ", f"<@!{me.id}> "]
        if spaced is not False
        else [f"<@{me.id}>", f"<@!{me.id}>"]
    )
    return mentions


# for anyone running mypy, there is a lot of errors here...
# i am too lazy to fix them so i will just ignore it,
# if you find whats wrong you can just make a PR!
class Bot(hikari.GatewayBot):
    """A subclass of :class:`hikari.GatewayBot` adding functionality like
    command handling and voice while keeping the features of GatewayBot.

    Parameters
    ----------
    command_prefix
        The bots command prefix
    """

    def __init__(
        self, token: str, command_prefix: str = on_mention, **kwargs: t.Any
    ) -> None:
        self.command_prefix = command_prefix
        if "banner" not in kwargs:
            kwargs["banner"] = "expo"  # We do a little cool
        super().__init__(token, **kwargs)

    def command(self) -> Command:
        """The command creator.

        returns
        -------
        :class:`Command`
        """
        return Command

    def get_prefix(self):
        """returns the bots command prefix

        returns
        -------
        :class:`commands.Bot.command_prefix`
        """
        return self.command_prefix
