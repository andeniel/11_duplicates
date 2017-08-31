import argparse
import sys
import os
import hashlib


def get_hash_file(file_path, block_size=65536):
    with open(file_path, 'rb') as file_data:
        hasher = hashlib.md5()
        buffer = file_data.read(block_size)
        while buffer:
            hasher.update(buffer)
            buffer = file_data.read(block_size)
        return hasher.hexdigest()


def print_duplicates(duplicates):
    if duplicates:
        print("\nДубликаты найдены:")
        print(
            "Эти файлы одинаковые. Названия файлов могут быть разными,"
            " но содержание одинаковое:\n")
        for duplicate in duplicates:
            print("--- одинаковые файлы ---")
            for file_path in duplicate:
                print(file_path)
            print("\n")
    else:
        print("\nДубликаты не найдены.")


def get_duplicates(folder_path):
    duplicates = {}
    for dir_name, _, file_list in os.walk(folder_path):
        for file_name in file_list:
            file_path = os.path.join(dir_name, file_name)
            file_hash = get_hash_file(file_path)
            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]

    return list(filter(lambda x: len(x) > 1, duplicates.values()))


if __name__ == '__main__':
    aparser = argparse.ArgumentParser()
    aparser.add_argument(
        "-f", "--folder", required=True, help="Путь к папке")
    args = aparser.parse_args()
    duplicates = get_duplicates(args.folder)
    print_duplicates(duplicates)
