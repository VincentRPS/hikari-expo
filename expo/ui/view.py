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
import sys
import typing as t
from itertools import groupby

from .item import Item


class _ViewWeights:
    def __init__(self, children: t.List[Item]):
        self.weights: t.List[int] = [0, 0, 0, 0, 0]

        key: lambda i: sys.maxsize if i.row is None else i.row
        children = sorted(children, key=key)
        for row, group in groupby(children, key=key):
            for item in group:
                self.add_item(item)

    def find_open_space(self, item: Item) -> int:
        for index, weight in enumerate(self.weights):
            if weight + item.width <= 5:
                return index

        raise ValueError("Could not find open space for item!")

    def add_item(self, item: Item):
        if item.row is not None:
            total = self.weights[item.row] + item.width
            if total > 5:
                raise ValueError(f"Item cant fit in row {item.row} ({total} > 5)")
        else:
            # TODO: this
            ...


class View:
    """Represents a UI view."""
