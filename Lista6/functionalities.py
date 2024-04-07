import re
import datetime
def parse_entry(entry):
    match = re.search(
        r'(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<application>\w+)\[(?P<pid>\d+)]: (?P<event>.+)',
        entry)
    if match:
        return (datetime.strptime(match.group('timestamp'), "%b %d %H:%M:%S"),match.group('hostname'), int(match.group('pid')), match.group('event'))
    else:
        return None
