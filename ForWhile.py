#반복문

for waiting_num in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting_num))

for waiting_num in range(1,6) :  #1~5까지 범위
    print("대기번호: {0}".format(waiting_num))


starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))




# while문
customer = "토르"
index =5
while index >=1: #조건이 만족될때까지 반복
    print("{0} 커피가 준비 되었습니다.{1} 번 남았습니다.".format(customer,index))
    index-=1 #index-1를 index에 할당
    if index == 0:
        print("커피는 폐기처분되었습니다.")



# customer = "아이언맨"
# index = 1
# while True:
#     print("{0} 커피 나왔습니다.호출{1}".format(customer,index))
#     index+=1 #무한 루프에 빠지게 된다. ctrl + c를 누르면 강제 종료


customer = "다람쥐"
person = "nu"
while person != "다람쥐": #같지 않으면 while문 실행   같으면 탈출
 print("{0} 커피 나왔습니다.".format(customer))
 person=input("손님 이름이 어떻게 되시나요? ")
