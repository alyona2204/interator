import json
from hashlib import md5

file_list = []

class Myrange:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file, encoding='utf-8') as new_file:
            list_name = json.load(new_file)
            for items in list_name:
                сountry = items['translations']['rus']['common']
                file_list.append(сountry)
                url = 'https://ru.wikipedia.org/wiki' + '/' + сountry
                file_list.append(url)
            with open("list.txt", "a") as f:
                print(file_list, file=f)


    def encoding(self):
        for elem in file_list:
            elem_md5 = md5(elem.encode()).hexdigest()
            with open("result_md5.txt", "a") as f:
                print(elem_md5, file=f)


if __name__ == '__main__':
    file_json = Myrange('countries.json')
    file_json.__next__()
    file_json.encoding()




