from functionalities import create_log_list, create_logger, group_by_user, get_statistics_for_log
import random
import statistics

logger = create_logger()


def zad4a(file_dir, n: int):
    list_of_entries = create_log_list(file_dir, logger)
    user_entries_map = group_by_user(list_of_entries)
    random_user = random.choice(list(user_entries_map.keys()))
    random_user_list = [entry.content for entry in user_entries_map[random_user]]
    n = min(n, len(random_user_list))
    random_contents = random.sample(random_user_list, n)
    return {random_user: random_contents}


def zad4b(file_dir, global_=True):
    list_of_entries = create_log_list(file_dir, logger)
    if global_:
        return get_statistics_for_log(list_of_entries)
    else:
        user_entry_map = group_by_user(list_of_entries)
        return_dict = {}
        for user, entries in user_entry_map.items():
            print(entries)
            return_dict[user] = get_statistics_for_log(entries)
    return return_dict


def zad4c(file_dir):
    list_of_entries = create_log_list(file_dir, logger)
    user_entry_map = group_by_user(list_of_entries)
    most_frequent_user = max(user_entry_map, key=lambda user: len(user_entry_map[user]))
    least_frequent_user = min(user_entry_map, key=lambda user: len(user_entry_map[user]))
    return {"Most Frequent: ": (most_frequent_user, len(user_entry_map[most_frequent_user])),
            "Least Frequent: ": (least_frequent_user, len(user_entry_map[least_frequent_user]))}


