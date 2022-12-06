from shutil import copyfile
from pathlib import Path

from requests import get


def create_data_file(day):
    x = get(
        f'https://adventofcode.com/2022/day/{day}/input',
        cookies={
            'session': '53616c7465645f5f5c5ae5005180667d012a44b8a090d5f817c2a19ea472f51c'
                       '6ec6617b321f9b73c83ecd3aa8ca71eff454bbc00c45bd2a50cf6c76563e7ab1'
        }
    )
    f = open(f'day{day}/day_{day}', 'x')
    f.write(x.text)


def create_test_data_file(day):
    open(f'day{day}/day_{day}_test', 'x')


def create_py_file(day):
    copyfile('py_init_template.py', f'day{day}/day_{day}.py')


def create_dir(day):
    Path(f'day{day}').mkdir()


if __name__ == '__main__':
    day = 6
    create_dir(day)
    create_data_file(day)
    create_test_data_file(day)
    create_py_file(day)