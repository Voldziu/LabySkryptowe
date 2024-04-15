from Lab6_v2.functionalities import parse_log, get_ipv4s_from_log
import ipaddress
from abc import ABC, abstractmethod


class SSHLogEntry(ABC):
    def __init__(self, entry):
        self.time, self.hostname, self.pid, self.event = parse_log(entry)
        self._raw_entry = entry

    def __str__(self):
        return f"time: {self.time}, hostname: {self.hostname}, pid: {self.pid}, event: {self.event}"

    def __repr__(self):
        return f"{type(self).__name__}(time='{self.time}', hostname='{self.hostname}', pid='{self.pid}', event='{self.event}')"

    def __eq__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.pid == other.pid
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.time > other.time
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.time < other.time
        return NotImplemented

    def get_ip_object(self):
        entry_ip = get_ipv4s_from_log(self.event)

        if entry_ip:
            return ipaddress.IPv4Address(entry_ip[0])

        else:
            return None

    @abstractmethod
    def validate(self):
        pass

    @property
    def has_ip(self):
        return self.get_ip_object() is not None

    def get_raw_entry(self):
        return self._raw_entry


