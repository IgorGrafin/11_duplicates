import os
import sys
import collections


def make_files_location_dict(path):
    files_location_dict = collections.defaultdict(list)
    tree = os.walk(path)
    for cur_folder, subfolders, files_names in tree:
        for file_name in files_names:
            full_path = os.path.join(cur_folder, file_name)
            file_size = os.path.getsize(full_path)
            files_location_dict[file_name, file_size].append(full_path)
    return files_location_dict


def print_results(files_location_dict):
    # for file_name, file_size in files_location_dict:
    for (file_name, file_size), paths in files_location_dict.items():
        files_number = len(paths)
        if files_number > 1:
            print("Found {0} files {1} with size {2} :".format
                (
                files_number,
                file_name,
                file_size
            ))
            print("\n".join(paths))


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        sys.exit("Please, put a folder path as a parameter.\n"
                 "For example: 'python duplicates.py E:\GitHub' ")
    files_location_dict = make_files_location_dict(path)
    if not files_location_dict:
        print("Nothing found in {}".format(path))
        sys.exit(0)
    print_results(files_location_dict)
