from datetime import timedelta
from functionalities import create_log_list, get_message_type, get_ipv4s_from_log, get_user_from_log,read_logs,create_logger
from collections import defaultdict

def detect_bruteforce(path, consecutive_attempts_threshold=10, interval_seconds=5, target_single_user=True):

    detected_attacks =[]
    current_suspect_ip=None
    current_suspect_user=None #always none if target_single_user = False
    consecutive_attempts = 0
    last_attempt_time = None
    start_attempt_time=None
    suspected_users=set()

    def check_and_append():

        if (consecutive_attempts > consecutive_attempts_threshold):
            detected_attacks.append((start_attempt_time, entry.date, (current_suspect_ip, suspected_users), consecutive_attempts,))

    for entry in read_logs(path,None):
        if get_message_type(entry.content) == 'logging unsuccessful':
            ip_list = get_ipv4s_from_log(entry) # len<2
            if ip_list:
                ip = ip_list[0]
                user = get_user_from_log(entry)
                suspected_tuple = (ip,user) if target_single_user else (ip,None)
                if suspected_tuple == (current_suspect_ip,current_suspect_user):
                    #checking two things at time,
                    # if target_single_user = False, it checks only ip

                    suspected_users.add(user)
                    if last_attempt_time and entry.date - last_attempt_time < timedelta(seconds=interval_seconds):
                        consecutive_attempts += 1
                    else: #streak ends with reaching max_interval
                        check_and_append()
                        consecutive_attempts=1
                        start_attempt_time=entry.date
                        suspected_users={user} if user else set()
                        current_suspect_ip=ip
                else: #streak ends with ip (or user)  change

                    check_and_append()
                    consecutive_attempts = 1
                    suspected_users = {user}
                    current_suspect_user = user if target_single_user else None
                    start_attempt_time=entry.date
                    current_suspect_ip = ip
                #print(f'ip: {ip}, consecutive_attempts: {consecutive_attempts}, date: {entry.date}')
                last_attempt_time=entry.date
    check_and_append()
    return detected_attacks


if __name__ == '__main__':

    detected_att = detect_bruteforce('SSH.log',target_single_user=False)
    for element in detected_att:
        print(element)