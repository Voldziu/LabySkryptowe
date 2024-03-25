# backup.py

import os
import sys
from backup_utils import backup_directory, update_backup_history


def run():
    if len(sys.argv) != 2:
        print("Usage: python backup.py <directory_path>")
        sys.exit(1)

    source_dir = sys.argv[1]  # gets the path of folder in which files for backup are
    backup_dir = os.environ.get('BACKUPS_DIR', os.path.join(os.path.expanduser('~'),
                                                            '.backups'))  # gets the path of backup destination folder

    extension = 'tar.gz'

    backup_filename = backup_directory(source_dir, backup_dir, extension)  # returns the name of the folder with
    # zip/tar.gz extension
    update_backup_history(backup_dir, backup_filename, source_dir)  # updates history in backup_history.json file

    print(f"Backup of {source_dir} created in {backup_dir}")
    print(f"Backup history updated in {backup_dir}/backup_history.json")


if __name__ == "__main__":
    run()
