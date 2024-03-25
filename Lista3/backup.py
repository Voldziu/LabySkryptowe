# backup.py

import os
import sys
from backup_utils import backup_directory, move_backup_to_destination, update_backup_history


def run():
    if len(sys.argv) != 2:
        print("Usage: python backup.py <directory_path>")
        sys.exit(1)

    source_dir = sys.argv[1]
    backup_dir = os.environ.get('BACKUPS_DIR', os.path.join(os.path.expanduser('~'), '.backups'))

    extension = 'zip'

    backup_path, backup_filename = backup_directory(source_dir, os.getcwd(), extension)
    final_backup_path = move_backup_to_destination(backup_path, backup_dir)

    update_backup_history(backup_dir, backup_filename, source_dir)

    print(f"Backup of {source_dir} created in {backup_dir}")
    print(f"Backup history updated in {backup_dir}/backup_history.json")


if __name__ == "__main__":
    run()
