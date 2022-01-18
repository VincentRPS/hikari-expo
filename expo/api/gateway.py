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
# because the voice gateway is on a different version, it needs to be rebuilt for expo.
# this is in no way finished.
import json
import struct
from asyncio import AbstractEventLoop
from logging import getLogger

import aiohttp  # type: ignore

_log = getLogger(__name__)

GATEWAY: str = "wss://gateway.discord.gg/?v=4"


class VoiceGateway:
    # This is the reason every hikari lavalink extension is
    # in rust btw, the gateway is hard to make with python.
    """Represents the Gateway between discord and your bot
    within voice standards,
    It also interacts with your :class:`api.VoiceClient`
    """

    def __init__(self, loop):
        self.__session = aiohttp.ClientSession()
        self.loop: AbstractEventLoop = loop
        self.init: bool = False

    async def connect(self):
        self.ws = await self.__session.ws_connect(GATEWAY)
        self.loop.create_task(self.receive())

    async def send(self, data: dict):
        _log.debug("< %s", data)
        await self.ws.send_str(json.dumps(data))

    async def resume(self, server_id, token, session_id):
        payload = {
            "op": 0,
            "d": {
                "server_id": str(server_id),
                "token": token,
                "session_id": session_id,
            },
        }
        await self.send(payload)

    async def identify(self, server_id, token, user_id, session_id):
        payload = {
            "op": 0,
            "d": {
                "server_id": str(server_id),
                "user_id": str(user_id),
                "token": token,
                "session_id": session_id,
            },
        }
        await self.send(payload)

    async def receive(self):
        # This is TODO aswell
        for msg in self.ws:
            ...

    async def init(self, data):
        # Still TODO
        packet = bytearray(70)
        struct.pack_into(">H", packet, 0, 1)
        struct.pack_into(">H", packet, 2, 70)
        struct.pack_into(">I", packet, 4, data["ssrc"])
        # recv = await self.loop.sock_recv()
        ...

    async def select(self, ip, port, mode):
        payload = {
            "op": 1,
            "d": {
                "protocol": "udp",
                "data": {"address": ip, "port": port, "mode": mode},
            },
        }
        await self.send(payload)

    async def speak(self):
        payload = {"op": 5, "d": {"speaking": 1, "delay": 0}}
        await self.send(payload)
