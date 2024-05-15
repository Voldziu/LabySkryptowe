import re
from re import Match
from typing import Optional, Tuple, Iterator, List, Dict
from regexes import analysis_regexes, parse_log_regex, ipv4_regex
from datetime import datetime
from typing import List, Optional
import ipaddress
from abc import ABC, abstractmethod


class SSHLogEntry(ABC):
    def __init__(self, entry: str):

        self.time: datetime
        self.hostname: str
        self.pid: int
        self.event: str
        entry_parsed = parse_log(entry)
        if entry_parsed is not None:
            self.time, self.hostname, self.pid, self.event = entry_parsed
        else:
            self.time = datetime.max
            self.hostname = "Default"
            self.pid = -1
            self.event = "Default"
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
        entry_ip: Optional[str] = get_ipv4s_from_log(self.event)
        if entry_ip:
            return ipaddress.IPv4Address(entry_ip)
        return None

    @abstractmethod
    def validate(self) -> bool:
        pass

    @property
    def has_ip(self) -> bool:
        return self.get_ip_object() is not None

    def get_raw_entry(self) -> str:
        return self._raw_entry


def parse_log(entry: str) -> Optional[Tuple[datetime, str, int, str]]:
    match = re.search(parse_log_regex, entry)
    if match:
        return (datetime.strptime(match.group('timestamp'), "%b %d %H:%M:%S"),
                match.group('hostname'),
                int(match.group('pid')),
                match.group('event'))
    else:
        return None


def get_logs(path: str) -> Iterator[str]:
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def get_ipv4s_from_log(content: str) -> Optional[str]:
    match = re.search(ipv4_regex, content)
    if match:
        for i in range(1, 5):
            if int(match.group(i)) > 255:
                return None
        return str(match.group())
    else:
        return None


def get_user_from_log(log_entry: SSHLogEntry) -> Optional[str]:
    content = log_entry.event
    black_list_words = ['request', 'support', 'invalid']
    exclude_pattern = '|'.join(black_list_words)

    user_space_pattern = re.compile(r'user\s{1}((?!' + exclude_pattern + r')\w+)')
    user_equals_pattern = re.compile(r'user=([^\s]+)')
    patterns = [user_equals_pattern, user_space_pattern]

    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None


def group_by_user(list_of_log_entries: List[SSHLogEntry]) -> Dict[str, List[SSHLogEntry]]:
    user_entries_map: Dict[str, List[SSHLogEntry]] = {}
    for log_entry in list_of_log_entries:
        user = get_user_from_log(log_entry)
        if user:
            if user in user_entries_map:
                user_entries_map[user].append(log_entry)
            else:
                user_entries_map[user] = [log_entry]
    return user_entries_map
