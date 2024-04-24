import re

analysis_regexes = {
    "failed password": re.compile(r"^(Failed password for) .* from (\d+\.\d+\.\d+\.\d+) port (\d+) ssh2$"),
    "accepted password": re.compile(r"^(Accepted password for) .* from (\d+\.\d+\.\d+\.\d+) port (\d+) ssh2$"),
    "error": re.compile(r'^error:.*$')
}

date_time_regex = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-2]?[1-9]|10|20|30|31) ([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$")
ipv4_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
user_validation_regex = re.compile(r'^[a-z_][a-z0-9_-]{0,31}$')

parse_log_regex = re.compile(r'(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<application>\w+)\[(?P<pid>\d+)]: (?P<event>.+)')

