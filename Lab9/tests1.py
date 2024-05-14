import pytest
from datetime import datetime

from ssh_entry_functionalities import SSHLogEntry
from Zad2 import Other


def test_time_extraction():
    entry = "Dec 10 06:55:46 LabSZ sshd[24200]: Invalid user webmaster from 173.234.31.186"
    ssh_log_entry = Other(entry)
    assert ssh_log_entry.time == datetime(1900, 12, 10, 6, 55, 46)


def test_invalid_log_entry():
    entry = "Invalid log entry"
    ssh_log_entry= Other(entry)

    assert ssh_log_entry.time == datetime.max


def test_empty_log_entry():
    entry = ""
    ssh_log_entry = Other(entry)
    assert ssh_log_entry.time ==datetime.max

