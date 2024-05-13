from datetime import datetime
from typing import List, Optional
import ipaddress
from abc import ABC, abstractmethod
from functionalities import parse_log, get_ipv4s_from_log


class SSHLogEntry(ABC):
    def __init__(self, entry: str):
        self.time: datetime
        self.hostname: str
        self.pid: int
        self.event: str
        self.time, self.hostname, self.pid, self.event = parse_log(entry)
        self._raw_entry: str = entry

    def __str__(self) -> str:
        return f"time: {self.time}, hostname: {self.hostname}, pid: {self.pid}, event: {self.event}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(time='{self.time}', hostname='{self.hostname}', pid='{self.pid}', event='{self.event}')"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SSHLogEntry):
            return self.pid == other.pid
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, SSHLogEntry):
            return self.time > other.time
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, SSHLogEntry):
            return self.time < other.time
        return NotImplemented

    def get_ip_object(self) -> Optional[ipaddress.IPv4Address]:
        entry_ip: List[str] = get_ipv4s_from_log(self.event)
        if entry_ip:
            return ipaddress.IPv4Address(entry_ip[0])
        return None

    @abstractmethod
    def validate(self) -> bool:
        pass

    @property
    def has_ip(self) -> bool:
        return self.get_ip_object() is not None

    def get_raw_entry(self) -> str:
        return self._raw_entry





