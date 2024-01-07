#!/usr/bin/python3
#encoding=utf-8

#첫째 줄의 내용은 프로그램 실행 시 해당 경로의 프로그램을 활용하라는 참고이다.
#두 번째 줄의 내용은 인코딩 오류를 막기 위한 참고이다.

# Find 'ok' in files and write on 'result.txt'

import sys
import pathlib

def get_path():
    #count = 0
    s_path = pathlib.Path(sys.argv[1])
    for i in s_path.glob('*.py'):
        # print(i.as_posix())
        with open(i.as_posix(), 'r') as fp:
            print(fp.readlines())
            if 'ok' in map(lambda x: x.strip('\n'), fp.readlines()):
                with open("/home/rapa/result.txt", 'w') as result:
                    result.write(fp_lst)

get_path()