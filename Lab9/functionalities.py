import re
from datetime import datetime
from regexes import analysis_regexes, parse_log_regex, ipv4_regex


def parse_log(entry):
    match = re.search(
        parse_log_regex, entry)
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
    matches = re.findall(ipv4_regex, content)
    return matches


def get_user_from_log(log_entry):
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


def group_by_user(list_of_log_entries):
    user_entries_map = {}
    for log_entry in list_of_log_entries:
        user = get_user_from_log(log_entry)
        if user:
            if user in user_entries_map:
                user_entries_map[user].append(log_entry)
            else:
                user_entries_map[user] = [log_entry]
    return user_entries_map


