from Zad1 import SSHLogEntry
from Lab6_v2.regexes import analysis_regexes
import re
from Lab6_v2.functionalities import get_logs


class PasswordFail(SSHLogEntry):
    def __init__(self, entry):
        super().__init__(entry)

    def validate(self):
        match = re.match(analysis_regexes['accepted password'], self.event)

        if match:
            return True
        else:
            return False


class PasswordAccepted(SSHLogEntry):
    def __init__(self, entry):
        super().__init__(entry)

    def validate(self):
        match = re.match(analysis_regexes['failed password'], self.event)

        if match:
            return True
        else:
            return False


class Error(SSHLogEntry):
    def __init__(self, entry):
        super().__init__(entry)

    def validate(self):
        match = re.match(analysis_regexes['error'], self.event)

        if match:
            return True
        else:
            return False


class Other(SSHLogEntry):
    def __init__(self, entry):
        super().__init__(entry)

    def validate(self):
        return True


if __name__ == '__main__':
    generator = get_logs('../SSH.log')
    entrySSH = Other(next(generator))
    print(entrySSH.validate())

    line = next(generator)
    print(f"\nLine: {line}")
    entry_SSH_accepted = PasswordAccepted(line) # returns False, wrong object
    print(f"Has IP: {entry_SSH_accepted.has_ip}")
    print(entry_SSH_accepted.validate())

    entry_SSH_error = Error(line)
    print(entry_SSH_error.validate()) # returns true, it is indeed an error log

    next_line = next(generator)
    entry_SSH_error_2 = Error(next_line)
    print(f"Next line: {next_line}")

    print(f"line and next_line are equal: {entry_SSH_error==entry_SSH_error_2}")
    print(f"line is greater than next_line: {entry_SSH_error>entry_SSH_error_2}") # both have the same dates
    print(f"line is lesser than next_line: {entry_SSH_error<entry_SSH_error_2}")


