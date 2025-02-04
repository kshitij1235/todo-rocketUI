from copy import copy
from vendor.Rocket import log

from copy import copy
from vendor.Rocket import log
from typing import Literal


class SaveState:

    def __init__(self):
        self._storage: dict = {"global": []}
        self._keys: list = ["global"]

    def UpdateKeys(self) -> None:
        self._keys = list(self._storage.keys())

    def CreateNewMemorySection(self, section_name: str = ""):
        if section_name not in self._storage:
            self._storage[section_name] = {}
            self.UpdateKeys()

    def ReleaseSection(self, section_name: str = ""):
        if section_name == "global":
            log("cannot release global memory")
            return
        if section_name in self._storage:
            del self._storage[section_name]
            self.UpdateKeys()

    def AccessMemorySection(self, section_name: Literal["global", "local", "cache"] = "global"):
        return copy(self._storage.get(section_name, []))

    def AccessMemorySectionVar(self, section_name: str, key: str) -> str:
        if section_name in self._keys:
            return copy(self._storage.get(section_name, {}).get(key, ""))
        else:
            log("Memory section not found")
            return ""
            
