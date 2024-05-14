import pytest
from Zad2 import Other,PasswordFail, PasswordAccepted, Error
from Zad7 import SSHLogJournal



@pytest.mark.parametrize("entry, expected_type", [
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2", PasswordFail),
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Accepted password for user from 173.234.31.186 port 38926 ssh2", PasswordAccepted),
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Some other log message", Other),
    ("Dec 10 09:11:34 LabSZ sshd[24447]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]",Error)

])
def test_add_entry(entry, expected_type):
    ssh_log_journal = SSHLogJournal()
    ssh_log_journal.add_entry(entry)
    assert isinstance(ssh_log_journal.log_journal[-1], expected_type)