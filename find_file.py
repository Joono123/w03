#!/usr/bin/python3
#encoding=utf-8

#첫째 줄의 내용은 프로그램 실행 시 해당 경로의 프로그램을 활용하라는 참고이다.
#두 번째 줄의 내용은 인코딩 오류를 막기 위한 참고이다.

# Find 'ok' in files and write on 'result.txt'

import sys
import pathlib
import re
import time
import os

keyword = input("검색어를 입력하세요 : ")

def get_path():
    home = pathlib.Path.home()
    home_path = '{0}/{1}'.format(home.as_posix(), 'result.txt')
    count = 0
    try:
        s_path = pathlib.Path(sys.argv[1])
        for i in s_path.glob('**/*.py'):
            if count > 5:
                break
            with open(i.as_posix(), 'r') as fp:
                # fp.readlines() --> list
                try:
                    for rl in fp.readlines():
                        res = re.search(keyword, rl) # 'ok'자리에 다른 문자열 입력 가능
                        # ok 단어를 못 찾았다면,
                        if res is None:
                            continue
                        with open(home_path, 'a') as fp2:
                            fp2.write('\n파일명 : {0} \n경로 : {1} \n내용 : {2}\n'.format(i.name, i.as_posix(), rl))
                except UnicodeDecodeError as err:
                    pass
        with open(home_path, 'a') as today:
            today.write('찾은 시간 : {0}\n\n'.format(time.strftime('%c', time.localtime(time.time()))))
        with open(home_path, 'a') as multiline:
            multiline.write('='*50)
    except IndexError as err:
        sys.stderr.write('index가 잘못됨')


get_path()
