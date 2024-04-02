from functionalities import *


def Zad2a(file_dir):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)
    return list_of_logEntries


def Zad2b(file_dir):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)

    return [get_ipv4s_from_log(entry) for entry in list_of_logEntries]


def Zad2c(file_dir):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)

    return [get_user_from_log(entry) for entry in list_of_logEntries]

def Zad2d(file_dir):
    log = read_shh(file_dir)
    list_of_logEntries = convert_into_tuples(log)

    return [get_message_type(entry.content) for entry in list_of_logEntries]
