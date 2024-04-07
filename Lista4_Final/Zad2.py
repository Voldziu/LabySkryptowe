from functionalities import create_log_list, create_logger, get_ipv4s_from_log, get_user_from_log, get_message_type, read_logs


logger = create_logger()


def zad2a(path):
    list_of_entries = create_log_list(path, logger)
    return list_of_entries


def zad2b(path):
    for line in read_logs(path, logger, True):
        print(get_ipv4s_from_log(line))


def zad2c(path):
    for line in read_logs(path, logger):
        print(get_user_from_log(line))


def zad2d(path):
    for line in read_logs(path, logger, True):
        print(get_message_type(line.content))


