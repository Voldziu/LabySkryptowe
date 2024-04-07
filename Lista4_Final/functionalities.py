from datetime import datetime
from collections import namedtuple
import re
import statistics
from constantsAndPaterns import logging_patterns
import logging
import sys

Log = namedtuple('LogEntry', ['date', 'id', 'content'])
Stats = namedtuple('Stats', ['mean', 'std'])


def create_logger():
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)

    standard_handler = logging.StreamHandler(sys.stdout)
    standard_handler.setLevel(logging.DEBUG)
    standard_formatter = logging.Formatter('%(levelname)s: %(message)s')
    standard_handler.setFormatter(standard_formatter)

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(standard_formatter)
    logger.addHandler(error_handler)
    logger.addHandler(standard_handler)
    return logger


def split_logs(log):
    match = re.search(
        r'(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<application>\w+)\[(?P<pid>\d+)]: (?P<event>.+)',
        log)

    if match:
        return Log(datetime.strptime(match.group(1), "%b %d %H:%M:%S").replace(year=2137), int(match.group(4)), match.group(5))
    else:
        return None


def read_logs(path, logger, log_entries=False):
    data_amount = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            log_entry = split_logs(line)

            if log_entry:
                data_amount += len(line.encode('utf-8'))
                if log_entries:
                    logger.debug(
                        f"Total amount of read data {data_amount}, this line had {len(line.encode('utf-8'))} bytes")
                    log_the_entry(log_entry.content, logger)

                yield log_entry


def create_log_list(path, logger, log_entries=False):
    log_list = []
    for line in read_logs(path, logger, log_entries):
        log_list.append(line)

    return log_list


def get_ipv4s_from_log(log_entry_content):
    matches = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', log_entry_content)
    return matches


def get_message_type(event_description):
    patterns = logging_patterns

    for message_type, pattern in patterns.items():
        if pattern.search(event_description):
            return message_type

    return 'other'


def log_the_entry(event_description, logger):
    patterns = logging_patterns

    for message_type, pattern in patterns.items():
        if pattern.search(event_description):
            if message_type == 'logging successful' or message_type == 'disconnect':
                logger.info(" " + message_type)

            elif message_type == 'logging unsuccessful':
                logger.warning(" " + message_type)

            elif message_type == 'invalid password' or 'invalid username':
                logger.error(" " + message_type)

            elif message_type == 'break in attempt':
                logger.critical(" " + message_type)


def get_user_from_log(log_entry):
    content = log_entry.content
    black_list_words = ['request', 'support', 'invalid']
    exclude_pattern = '|'.join(black_list_words)

    user_space_pattern = r'user\s{1}((?!' + exclude_pattern + r')\w+)'
    user_equals_pattern = r'user=([^\s]+)'
    patterns = [user_equals_pattern, user_space_pattern]

    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None


def get_statistics_for_log(list_of_log_entries):
    current_id = None
    first_date = None
    last_date = None
    id_dates = []
    for log_entry in list_of_log_entries:
        if current_id == log_entry.id:
            last_date = log_entry.date
        else:
            if current_id:
                id_dates.append((current_id,first_date,last_date))
            current_id = log_entry.id
            first_date = log_entry.date
            last_date = log_entry.date
    if current_id:
        id_dates.append((current_id, first_date, last_date))

    list_of_connection_times= [(end_date - start_date).total_seconds() for log_id, start_date, end_date in id_dates]
    print(id_dates)
    print(list_of_connection_times)

    return Stats(statistics.mean(list_of_connection_times), statistics.stdev(list_of_connection_times) if len(id_dates) != 1 else 0)


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