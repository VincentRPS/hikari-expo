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
from hikari.impl import VoiceComponentImpl
from hikari import Snowflakeish, SnowflakeishOr, GuildVoiceChannel
from hikari.api import VoiceConnection
from ..state import ConnectionState


class VoiceClient:
    """The client giving you easier control of :class:`api.VoiceGateway`
    within a easier client-like connection. while this class isn't needed,
    who wants to interact with raw json/opus audio?
    """
    def __init__(self, guild_id: Snowflakeish):
        self._voice = VoiceComponentImpl()
        self.connection = VoiceConnection()
        self.guild = guild_id
        self.state = ConnectionState()
        self.state.cache_thing(guild=guild_id)

    def leave(self):
        return self._voice.disconnect(self.guild)

