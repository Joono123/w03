#!/usr/bin/python3
#encoding=utf-8



# author : Juno Park


# def add():
#     a: int = int(input())
#     b: int = int(input())
#
# print(a)


# r: read
# w: write
# w: append

# f=open('test.txt', 'w')
# f.write('asdasdasdsd\n')
# f.write('dsaasdasdsd\n')
# f.write('sasdasdasdasdsd\n')
# f.close()

# f = open('test.txt', 'r')
# res = f.readlines()
# f.close()
#
# for i in res:
#     print(i.strip('\n'))

# with open('test.txt', 'w') as f:
#     f.write('tikrmedkd\n')
# print()

# 경로를 입력하면 해당 파일 리스트를 보여주는 스크립트
# 1. 스탠다드 모듈
# 2. 써드파티 모듈
# 3. 본인이 작성한 모듈

import sys
import pathlib


def get_path():
    count = 0
    try:
        s_path = pathlib.Path(sys.argv[1])
        for i in s_path.glob('**/*.py'):
            if count > 5:
                break
            with open(i.as_posix(), 'r') as fp:
                # fp.readlines() --> list
                try:
                    if 'ok' in fp.readlines():
                        print('found: ' + i.as_posix())
                        break
                except UnicodeDecodeError as err:
                    pass
    except IndexError as err:
        sys.stderr.write('index가 잘못됨')

get_path()

f.
