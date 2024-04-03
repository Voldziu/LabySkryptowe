from datetime import timedelta
from functionalities import create_log_list, get_message_type, get_ipv4s_from_log, get_user_from_log,read_logs,create_logger
from collections import defaultdict

def detect_bruteforce(path, consecutive_attempts_threshold=10, interval_seconds=5, target_single_user=True):




    detected_attacks =[]
    current_suspect_id=None
    current_suspect_user=None #always none if target_single_user = False
    consecutive_attempts = 0
    last_attempt_time = None
    suspected_users=set()

    def check_and_append(consecutive_attempts):
        if (consecutive_attempts > consecutive_attempts_threshold):
            detected_attacks.append((entry.date, (ip, suspected_users), consecutive_attempts))


    for entry in read_logs(path,None):
        if get_message_type(entry.content) == 'logging unsuccessful':
            ip_list = get_ipv4s_from_log(entry) #always one
            if ip_list:
                ip = ip_list[0]
                user = get_user_from_log(entry) #if target_single_user else ""
                suspected_tuple = (ip,user) if target_single_user else (ip,None)
                if suspected_tuple == (current_suspect_id,current_suspect_user):
                    suspected_users.add(user)
                    if last_attempt_time and entry.date - last_attempt_time < timedelta(seconds=interval_seconds):
                        consecutive_attempts += 1
                    else: #streak ends with reaching max_interval
                        check_and_append(consecutive_attempts)
                        consecutive_attempts=1
                        suspected_users={user} if user else set()
                else: #streak ends with ip (or user)  change
                    check_and_append(consecutive_attempts)
                    consecutive_attempts = 1
                    suspected_users = {user} if user else set()
                    current_suspect_user = user if target_single_user else None
                    current_suspect_id = ip
                #print(f'ip: {ip}, consecutive_attempts: {consecutive_attempts}, date: {entry.date}')
                last_attempt_time=entry.date
    check_and_append(consecutive_attempts)
    return detected_attacks


if __name__ == '__main__':

    detected_att = detect_bruteforce('SSH.log',target_single_user=False)
    for element in detected_att:
        print(element)