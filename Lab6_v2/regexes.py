import re

analysis_regexes = {
    "failed password": re.compile(r"^(Failed password for) .* from (\d+\.\d+\.\d+\.\d+) port (\d+) ssh2$"),
    "accepted password": re.compile(r"^(Accepted password for) .* from (\d+\.\d+\.\d+\.\d+) port (\d+) ssh2$"),
    "error": re.compile(r'authentication failure|invalid user|Invalid user|user unknown|error')
}

date_time_regex = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-2]?[1-9]|10|20|30|31) ([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$")
ipv4_regex = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")