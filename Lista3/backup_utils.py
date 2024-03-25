# backup_utils.py
import os
import json
import subprocess
import shutil
from datetime import datetime


def create_backup_folder(backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)


def get_backup_filename(source_dir, extension='zip'):
    dirname = os.path.basename(os.path.normpath(source_dir))
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    return f"{timestamp}-{dirname}.{extension}"


def backup_directory(source_dir, backup_dir, extension='zip'):
    backup_filename = get_backup_filename(source_dir, extension)
    backup_path = os.path.join(backup_dir, backup_filename)

    if extension == 'zip':
        command = ['7z', 'a', '-tzip', backup_path, source_dir]
    elif extension == 'tar.gz':
        command = ['tar', '-czf', backup_path, '.']
    else:
        raise Exception("Unsupported extension")

    subprocess.run(command, check=True, cwd=source_dir)

    return backup_path, backup_filename


def move_backup_to_destination(backup_path, destination_dir):
    create_backup_folder(destination_dir)
    final_path = shutil.move(backup_path, destination_dir)
    return final_path


def update_backup_history(backup_dir, backup_filename, source_dir):
    history_path = os.path.join(backup_dir, "backup_history.json")
    backup_record = {
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source_directory": source_dir,
        "backup_filename": backup_filename
    }

    if os.path.exists(history_path):
        with open(history_path, 'r') as file:
            history = json.load(file)
        history.append(backup_record)
    else:
        history = [backup_record]

    with open(history_path, 'w') as file:
        json.dump(history, file, indent=4)
