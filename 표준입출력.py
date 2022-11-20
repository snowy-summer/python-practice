print("python","Java", sep=",", end="?") #end는 마지막 문장을 ? 바꿔준다.
print("무엇이 더 재밌을까요?")

import sys
print("python","Java", file=sys.stdout) # 표준 출력으로 문장찍힘
print("python","Java", file=sys.stderr) #표준 에러로 찍힘    아직 이해가 안간다.


scores = {"수학": 0, "영어": 50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4), sep=":") # 과목은 총8칸의 공간에 왼쪽정렬 한다.
                                                         # 점수는 4칸에 우측정렬   sep는 ""와 ""사이에 : 채운다고 생각

#은행 대기 순번표 뽑기
#001,002,003
for num in range(1,21):
    print("대기번호 :"+str(num).zfill(3))   #zfill 3칸 확보하는데 없는 공간은 0으로


answer = input("아무값이나 입력하세요 :")
print("입력하신 값은 " + answer + "입니다.")  #숫자나  글자를 입력해도 잘나온다 이유는 둘다 str로 나온다.
# input 입력값은 항상 문자열로 나온다.



#-------------------------------------------------------------------
#--------------------------------------------------------------------
#다양한 출력포멧


print("{0: > 10}".format(500))  #{0: > 10} 빈공간 >우측정렬 10칸확보

#양수일 때 + 음수일 때 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))\

#왼쪽정렬 빈칸 _줄
print("{0:_<+10}".format(500))

#3자리마다 ,찍기
print("{0:,}".format(10000000000000000000000))
print("{0:+,}".format(-1000000000000000000))

#3자리마다 , 부호도 자릿수 확보하기  빈자리는 ^
print("{0:^<+20,}".format(5000000000)) #빈자리,정렬,부호,공간, 콤마

#소수점
print("{0:f}".format(5/3))

#특정자리 소수점
print("{0:.2f}".format(5/3)) # 소수점 둘째 자리


#파일 입출력
score_file = open("score.txt", "w", encoding="utf8")  #utf8정의 안해주면 한글 썻을때 이상하게 나올 수 잇음
print("수학: 0",file = score_file)
print("영어: 50",file = score_file)
score_file.close() # 파일을 열었을 때는 항상 닫아줘야 한다.

# 파일에 입력
score_file = open("score.txt", "a", encoding="utf8") # 내용이 존재하는 파일에 더 쓰고 싶으면 a
score_file.write("과학: 80")
score_file.write("\n코딩: 100") # write를 사용하면 자동으로 줄바꿈이 안되기 때문에 수동으로 줄바꿈을 넣어줘야 한다.
score_file.close()

# 파일 읽기
score_file = open("score.txt", "r", encoding= "utf8")
print(score_file.read())
score_file.close()

#파일 읽기 2
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기 , 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#파일 읽기 3
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)  # line을 한줄씩 읽는데 이제 없으면 멈춤
                 #줄바꿈 안하려면 end=""써주면 된다. print(line,end="")
score_file.close()



# 파일 읽기 4
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line,end="")

score_file.close()
