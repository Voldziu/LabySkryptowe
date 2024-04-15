import re
from datetime import datetime
from regexes import analysis_regexes


def parse_log(entry):
    match = re.search(
        r'(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<application>\w+)\[(?P<pid>\d+)]: (?P<event>.+)',
        entry)
    if match:
        return datetime.strptime(match.group('timestamp'), "%b %d %H:%M:%S"), match.group('hostname'), int(
            match.group('pid')), match.group('event')
    else:
        return None


def get_logs(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def get_ipv4s_from_log(content):
    matches = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', content)
    return matches


