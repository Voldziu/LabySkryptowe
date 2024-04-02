from datetime import datetime
from collections import namedtuple
import re
import statistics
LogEntry = namedtuple('LogEntry', ['date', 'id', 'content'])
Stats = namedtuple('Stats',['mean','std'])
def read_shh(file_dir):
    with open(file_dir,'r') as file:
        lines = file.readlines()
    return lines

def parse_log_line(log_line):

    regex_pattern = r'^([A-Za-z]+\s+\d+\s+\d+:\d+:\d+)\s+(LabSZ)\s+(sshd)\[(\d+)\]:\s+(.*)$'
    match = re.match(regex_pattern, log_line)
    if match:
        date = datetime.strptime(match.group(1), "%b %d %H:%M:%S")
        id = match.group(4)
        content = match.group(5)
        return LogEntry(date, id, content)
    else:
        return None

def convert_into_tuples(log):
    return_list=[]
    for entry in log:
        entry_parsed = parse_log_line(entry)
        return_list.append(entry_parsed)
    return return_list
def get_ipv4s_from_log(Log_Entry:LogEntry):
    content = Log_Entry.content
    regex_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_addresses = re.findall(regex_ip,content)
    return ip_addresses

def get_user_from_log(Log_Entry:LogEntry):
    content = Log_Entry.content
    black_list_words=['request','support','invalid']
    exclude_pattern='|'.join(black_list_words)

    user_space_pattern =r'user\s{1}((?!'+exclude_pattern + r')\w+)'
    user_equals_pattern = r'user=([^\s]+)'
    patterns = [user_equals_pattern,user_space_pattern]

    for pattern in patterns:
        match = re.search(pattern,content)
        if match:
            return match.group(1)
    return None



def get_message_type(content):
    patterns = {
        'login_passed': r'Accepted password for',
        'login_failed': r'authentication failure',
        'connection_closed': r'Connection closed',
        'password_failed': r'Failed password for',
        'invalid_user': r'invalid user',
        'break_in': r'POSSIBLE BREAK-IN'
    }

    for key, pattern in patterns.items():
        if re.search(pattern, content):
            return key
    return 'inne'

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

    list_of_connection_times=[ (end_date - start_date).total_seconds() for log_id, start_date, end_date in id_dates]
    print(id_dates)
    print(list_of_connection_times)

    return Stats(statistics.mean(list_of_connection_times), statistics.stdev(list_of_connection_times) if len(id_dates) != 1 else 0)



if __name__ =="__main__":
    log  = read_shh(r'C:\Users\Mikolaj\PycharmProjects\JSREPO\LabySkryptowe\Lista4\SSH.log')
    tuples = convert_into_tuples(log)
    for t in tuples:
        print(t.date)
