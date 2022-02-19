import json
from pprint import pprint


def read_local_file(file_today: str) -> dict:
    """
    only get data once every day, read data after get data from api
    :param file_today: local json filename
    :return: dict
    """
    from typing import NamedTuple
    data = json.load(open(file_today, encoding='utf-8'))
    return data

def query(word):
    url = 'https://dict.youdao.com/jsonapi?q=%s' % word
    import requests
    response = requests.get(url).text
    words = json.loads(response)
    chinese = words.get(
        'web_trans', {}).get('web-translation', [])[0].get(
        'trans', [])[0].get('value', '')
    return chinese



def main():
    chinese = query('again')
    # file_word = 'translation.json'
    # words = read_local_file(file_word)
    # chinese = words.get(
    #     'web_trans', {}).get('web-translation', [])[0].get(
    #     'trans', [])[0].get('value', '')

    print(chinese)



if __name__ == '__main__':
    main()