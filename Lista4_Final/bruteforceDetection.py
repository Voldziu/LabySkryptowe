from datetime import timedelta
from functionalities import create_log_list, get_message_type, get_ipv4s_from_log, get_user_from_log
from collections import defaultdict


def detect_bruteforce(log_list, consecutive_attempts_threshold=10, interval_seconds=5, target_single_user=True):
    attempts = defaultdict(list)

    for entry in log_list:
        if get_message_type(entry.content) == 'logging unsuccessful':
            ip_addresses = get_ipv4s_from_log(entry)
            user = get_user_from_log(entry) if target_single_user else ""
            for ip in ip_addresses:
                key = (ip, user) if target_single_user else ip
                attempts[key].append(entry.date)

    detected_attacks = []
    for key, timestamps in attempts.items():
        timestamps.sort()
        consecutive_attempts = 0
        for i in range(len(timestamps)-1):
            if timestamps[i+1] - timestamps[i] < timedelta(seconds=interval_seconds):
                consecutive_attempts += 1

            else:
                if consecutive_attempts > consecutive_attempts_threshold:
                    detected_attacks.append((timestamps[i-1], key[0], consecutive_attempts))

        if consecutive_attempts > consecutive_attempts_threshold:
            detected_attacks.append((timestamps[-1], key[0], consecutive_attempts))

    return detected_attacks


if __name__ == '__main__':
    log_list = create_log_list('SSH.log', None)
    detected_att = detect_bruteforce(log_list)
    for element in detected_att:
        print(element)