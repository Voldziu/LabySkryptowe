from functionalities import *
import random
import statistics
def Zad4a(file_dir,n:int):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)
    user_entries_map =group_by_user(list_of_logEntries)
    random_user = random.choice(list(user_entries_map.keys()))
    random_user_list = [entry.content for entry in user_entries_map[random_user]]
    n = min(n,len(random_user_list))
    random_contents = random.sample(random_user_list,n)
    return {random_user:random_contents}

def Zad4b(file_dir,Global=True):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)
    if Global:
        return get_statistics_for_log(list_of_logEntries)
    else:
        user_entry_map = group_by_user(list_of_logEntries)
        return_dict={}
        for user, entries in user_entry_map.items():
            print(entries)
            return_dict[user]=get_statistics_for_log(entries)
    return return_dict

def Zad4c(file_dir):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)
    user_entry_map = group_by_user(list_of_logEntries)
    most_frequent_user = max(user_entry_map, key=lambda  user: len(user_entry_map[user]))
    least_frequent_user = min(user_entry_map, key=lambda  user: len(user_entry_map[user]))
    return {"Most Frequent: ":(most_frequent_user,len(user_entry_map[most_frequent_user])),
                               "Least Frequent: ": (least_frequent_user,len(user_entry_map[least_frequent_user]))}



if __name__ =="__main__":
    print(Zad4a(r'C:\Users\Mikolaj\PycharmProjects\JSREPO\LabySkryptowe\Lista4\SSH.log'))

