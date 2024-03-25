import os
import sys
from restore_utils import list_backups, restore_backup


def main():
    backup_dir = sys.argv[1] if len(sys.argv) == 2 else os.path.join(os.path.expanduser('~'), '.backups')
    backup_dir = os.environ.get('BACKUPS_DIR', backup_dir)

    backups = list_backups(backup_dir)
    restore_backup(backup_dir, backups)


if __name__ == "__main__":
    main()
