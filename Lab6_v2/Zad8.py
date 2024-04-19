from regexes import user_validation_regex
import re


class SSHUser:
    def __init__(self, username, last_log_date):
        self.username = username
        self.last_log_date = last_log_date

    def validate(self):
        match = re.match(user_validation_regex, self.username)
        return match is not None




