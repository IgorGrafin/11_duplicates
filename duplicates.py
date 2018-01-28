import os


def make_files_dict(path):
    tree = os.walk(path)
    for cur_folder, subfolders, files in tree:
        for file in files:
            full_path = os.path.join(cur_folder, file)
            files_dict[full_path] = [file, os.path.getsize(full_path)]

    return files_dict


def find_duplicates(files_dict):
    duplicates_dict = {}
    for files in files_dict.keys():
        for key in files_dict.keys():
            if files != key\
                    and files_dict[files][0] == files_dict[key][0]\
                    and files_dict[files][1] == files_dict[key][1]:
                print(files)
                if not duplicates_dict.get(files_dict[key][0]):
                    duplicates_dict[files_dict[key][0]] = [key]
                else:
                    duplicates_dict[files_dict[key][0]].append(key)

    return duplicates_dict


if __name__ == '__main__':
    files_dict = {}

    path = "E:\\GitHub\\devman\\11_duplicates\\foldertest"

    files_dict = make_files_dict(path)
    # for x in files_dict.keys():
    #     print(x, files_dict[x])
    duplicates = find_duplicates(files_dict)

    for file_name in duplicates.keys():
        print("Одинаковые файлы ", file_name, "найдены по следующим адресам:")
        for file_path in duplicates[file_name]:
            print(file_path)