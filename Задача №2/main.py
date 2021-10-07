import hashlib


def returning_a_hash_of_strings(path_to_file):
    with open(path_to_file, "r", encoding='utf-8') as file:
        for line in file:
            line_hash = hashlib.md5(line.encode()).hexdigest()
            yield line_hash


if __name__ == '__main__':
    for line in returning_a_hash_of_strings('new_document.txt'):
        print(line)
         
