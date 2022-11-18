from random import *
cnt = 0 #총 탑승 승객
for i in range (1,51): #1~50 승객
    time = randrange(5,51)# 5~50분 무작위로 한개 얻는다.
    if 5 <= time <= 15:
        print("[o] {0}번쨰 손님 (소요시간 : {1}분)".format(i,time))
        cnt+=1 #탑승객 수를 세기 위해서 
    else :
        print("[x] {0}번째 손님 (소요시간: {1}분)".format(i,time))

print("총 탑승객 {0}분".format(cnt))
