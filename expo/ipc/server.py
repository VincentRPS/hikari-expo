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
# The server, webserver.
# Any WebSocket thing should work with this,
# e.g. flask, sanic, and aiohttp.


class Server:
    """The server requesting to the :class:`ipc.Client`"""

    def __init__(self, host, port, secret_key):
        ...
