import os
import sys


def make_files_dict(path):
    files_dict = {}
    tree = os.walk(path)
    for cur_folder, subfolders, files_names in tree:
        for file_name in files_names:
            full_path = os.path.join(cur_folder, file_name)
            file_size = os.path.getsize(full_path)
            if (file_name, file_size) in files_dict.keys():
                files_dict[file_name, file_size].append(full_path)
            else:
                files_dict[file_name, file_size] = [full_path]
    return files_dict


def beauty_print(files_dict):
    for file_name, file_size in files_dict:
        files_number = len(files_dict[file_name, file_size])
        if files_number > 1:
            print("Found {0} files {1} with size {2} :".format
                (
                files_number,
                file_name,
                file_size
            ))
            print("\n".join(files_dict[file_name, file_size]))


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        sys.exit("Please, put a folder path as a parameter.\n"
                 "For example: 'python duplicates.py E:\GitHub' ")
    files_dict = make_files_dict(path)
    if len(files_dict) == 0:
        sys.exit("Nothing found in {}".format(path))
    beauty_print(files_dict)
