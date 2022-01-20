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

# caches guilds and everything built into expo.
class ConnectionState:
    def __init__(self):
        self._cached_unknown = []
        self._cached_guilds = []
        self._cached_channels = []
        self._cached_voice_channels = []

    def cache_thing(self, **thing):
        if "guild" in thing:
            self._cached_guilds.append(thing.pop("guild"))
        elif "channel" in thing:
            self._cached_channels.append(thing.pop("channel"))
        elif "voice_channel" in thing:
            self._cached_voice_channels.append(thing.pop("voice_channel"))
        elif "unknown_cache" in thing:  # handles unknown objects, by not.
            self._cached_unknown.append(thing.pop("unknown_cache"))

    # i need to make a way to get cached items easily.
