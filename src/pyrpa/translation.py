import json
from typing import *


def read_local_file(file_today: str) -> Dict[str, Any]:
    """
    only get data once every day, read data after get data from api

    Args:
        file_today: local json filename

    Returns:
        python dict from local json file
    """
    data = json.load(open(file_today, encoding='utf-8'))
    return data


def query(word: str) -> str:
    """
    query word meaning from api

    Args:
        word: word need be translated

    Returns:
        chinese meaning for words.
    """
    url = 'https://dict.youdao.com/jsonapi?q=%s' % word
    import requests
    response: str = requests.get(url).text
    words: dict = json.loads(response)
    chinese: str = words.get(
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
