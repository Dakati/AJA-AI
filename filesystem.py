import os
import shutil

HOME = os.path.expanduser("~")


def find_file(filename):

    matches = []

    for root, dirs, files in os.walk(HOME):

        for file in files:

            if filename.lower() in file.lower():

                matches.append(os.path.join(root, file))

    return matches


def open_file(path):

    try:

        os.startfile(path)

        return "Opening file."

    except Exception as e:

        return str(e)


def create_folder(name):

    folder = os.path.join(HOME, name)

    os.makedirs(folder, exist_ok=True)

    return folder


def rename_file(old_path, new_name):

    folder = os.path.dirname(old_path)

    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

    return new_path