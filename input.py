#input : 사용자 입력 받는 함수
language = input("무슨 언어 좋아하세요?")
print("{0}은 좋은 언어 입니다.".format(language))


#dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir()) #random이 추가됨


print(dir(random)) # random 에서 사용가능한 내용이 나온다.

lst = [1,2,3]
print(dir(lst))  # list와 사용가능한 내용들이 나온다.

name = "aaaa"
print(dir(name)) # 스트링과 관련된 것들이 나온다.



#외장함수
#glob: 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일

#os : 운영체제에서 제공하는 기본 기능

import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder," 폴더를 삭제 하였습니다.")
else:

    os.makedirs(folder) #폴더 생성
    print(folder," 폴더를 생성하였습니다.")


#time : 시간관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %h:%M:%S")) #연 월 날짜  시간 분 초

import datetime
print("오늘 날짜는",datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난지 100일은",today + td)#오늘 부터 100일후