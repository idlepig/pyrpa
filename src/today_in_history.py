import json
import os
from datetime import datetime

import requests


def gen_today_file_name() -> str:
    """
    generate today json filename
    :return: filename, e.g.: today_in_history-*.json
    """
    now = datetime.now().strftime('%m-%d')
    file_today = 'today_in_history-%s.json' % now
    return file_today


def is_today_file_exist(file_today: str) -> bool:
    """
    check whether today_in_history-*.json file exist.
    :param file_today: today json filename
    :return: bool
    """
    return os.path.exists(file_today)


def format_data(data: dict) -> str:
    """
    join each title by \n
    :param data: json data
    :return: formatted text
    """
    raw = ['日期: ' + i.get('date', '') + ', 内容: ' + i.get('title', '') for i in
           data.get('result', [])]
    result = '\n'.join(raw)
    return result


def read_local_file(file_today: str) -> dict:
    """
    only get data once every day, read data after get data from api
    :param file_today: local json filename
    :return: dict
    """
    data = json.load(open(file_today, encoding='utf-8'))
    return data


def get_data() -> dict:
    """
    data source, use requests get data
    :return: dict
    """
    url = 'https://api.oick.cn/lishi/api.php'
    response = requests.get(url).text
    response = json.loads(response)
    return response


def write_local_file(file_today: str, data: dict) -> None:
    """
    store data to local file
    :param file_today: today json filename
    :param data: json data
    :return: None
    """
    json.dump(data, open(file_today, 'w', encoding='utf-8'))


def main():
    file_today = gen_today_file_name()
    today_file_exist = is_today_file_exist(file_today)

    if today_file_exist:
        print('local file exist, get data from local file: %s' % file_today)
        data = read_local_file(file_today)
    else:
        print('local file not exist, get data from api')
        data = get_data()
        write_local_file(file_today, data)

    data = format_data(data)
    print('\n-----------------------------')
    print(data)


if __name__ == '__main__':
    main()
