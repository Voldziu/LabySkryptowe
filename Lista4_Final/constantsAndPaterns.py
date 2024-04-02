import re

logging_patterns = {
        'logging successful': re.compile(r'successful login|accepted'),
        'logging unsuccessful': re.compile(r'authentication failure'),
        'disconnect': re.compile(r'closed connection|received disconnect|Connection closed|Received disconnect|Disconnecting'),
        'invalid password': re.compile(r'failed password for'),
        'invalid username': re.compile(r'invalid user|Invalid user|user unknown'),
        'break in attempt': re.compile(r'POSSIBLE BREAK-IN ATTEMPT!'),
    }