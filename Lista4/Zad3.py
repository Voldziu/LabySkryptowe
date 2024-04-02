import logging

from functionalities import *
import sys
def scan_log(file_dir,minlevel='DEBUG'):

    levels ={'DEBUG': logging.DEBUG,
              'INFO': logging.INFO,
              'WARNING': logging.WARNING,
              'ERROR': logging.ERROR,
              'CRITICAL': logging.CRITICAL}

    root_logger = logging.getLogger(__name__)
    root_logger.setLevel(levels.get(minlevel,logging.DEBUG))
    formatter = logging.Formatter('%(levelname)s: %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(formatter)

    root_logger.addHandler(stdout_handler)
    root_logger.addHandler(stderr_handler)

    with open(file_dir,'r',encoding='utf-8') as file:
        total_bytes=0

        for entry in file:
            entry = entry.rstrip()
            parsed_entry = parse_log_line(entry)
            content = parsed_entry.content
            message_type = get_message_type(content)
            current_bytes = len(entry.encode('utf-8'))
            total_bytes += current_bytes
            root_logger.debug(f'Total data read: {total_bytes} bytes, this line had {current_bytes} bytes')
            if message_type in ['login_passed','connection_closed']:
                root_logger.info("Successful login or connection closed")
            elif message_type == 'login_failed':
                root_logger.warning("Failed login attempt")
            elif message_type=='break_in':
                root_logger.critical("Possible break-in attempt")


if __name__ =="__main__":
    scan_log(r'C:\Users\Mikolaj\PycharmProjects\JSREPO\LabySkryptowe\Lista4\SSH.log')