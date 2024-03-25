import os
import json
import shutil
import subprocess
import sys


def list_backups(backup_dir):
    history_path = os.path.join(backup_dir, "backup_history.json")
    if not os.path.exists(history_path):
        print("No backups available.")
        sys.exit(1)

    with open(history_path, 'r') as file:
        backups = json.load(file)

    backups.sort(key=lambda x: x['date'], reverse=True)
    for index, backup in enumerate(backups, start=1):
        print(
            f"{index}. Date: {backup['date']}, Directory: {backup['source_directory']}, File: {backup['backup_filename']}")

    return backups


def restore_backup(backup_dir, backups):
    chosen_backup = int(input("Index of backup to restore: "))
    if chosen_backup < 1 or chosen_backup > len(backups):
        print("Incorrect Index.")
        sys.exit(1)

    backup = backups[chosen_backup - 1]
    archive_path = os.path.join(backup_dir, backup['backup_filename'])
    target_dir = backup['source_directory']

    if not os.path.exists(archive_path):
        print("Backup archive not found")
        sys.exit(1)

    print(f"Target dir {target_dir}")
    print(f"Archive path {archive_path}")

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Unable to delete {file_path}. Reason: {e}')

    if backup['backup_filename'].endswith('.zip'):
        command = ['7z', 'x', archive_path, '-o' + target_dir]
    elif backup['backup_filename'].endswith('.tar.gz'):
        command = ['tar', '-xzf', archive_path, '-C', target_dir]
    else:
        print("Unknown archive format.")
        sys.exit(1)

    subprocess.run(command, check=True)
    print("Restoring successful.")
