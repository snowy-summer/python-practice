# 함수 정의---------------------------------------------

def open_account():
    print("새로운 계좌가 생성되었습니다.") # 함수는 호출전까지는 출력이 안된다.
    
open_account()


#함수의 전달값과 반환값--------------------------------

def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance+money))
    return balance + money

balance = 0 #잔액
balance = deposit(balance,1000)   # 0원에 1000원을 더한뒤 반환을 해준 값이balance에 들어가게 된다.
print(balance)



def withdraw(balance,money):
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다.잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다 잔액은 {0} 원입니다.".format(balance))
        return balance



balance = 0
balance = deposit(balance,500)
balance = withdraw(balance,1000)
print(balance)




def withdraw_night(balance,money):
    commission = 100
    return commission, balance-money-commission

balance = 0
balance = deposit(balance,1000)
commission, balance = withdraw_night(balance,500)
print("수수료는 {0}원이며 잔액은 {1}원 입니다.".format(commission,balance))


# 함수의 기본값------------------------------------

def profile(name,age,main_lang):
    print("이름 :{0}\t나이 :{1}\t주 사용 언어: {2}".format(name,age,main_lang))  #줄바꿈은 역슬래쉬 엔터


profile("다람쥐",20,"파이썬")
profile("사자",25,"자바")



def profile(name,age=17,main_lang="파이썬"): # 같은 항목일 경우 값을 안받고 미리 통일 할 수 있다.
    print("이름 :{0}\t나이 :{1}\t주 사용 언어: {2}".format(name,age,main_lang))


profile("다람쥐")
profile("사자")



#키워드값--------------------------------------------
def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(name="다람쥐",main_lang="파이썬",age=20)
profile(main_lang="자바",age=28,name="사자")   # 다람쥐 10 파이썬
                                              # 사자 28 자바 로 출력이 된다. 


#가변인자----------------------------------------

def profile(name,age,lang1,lang2,lang3,lang4,lang5):
    print("이름: {0}\t나이: {1}\t".format(name,age),end=" ") #end= " " 를 적으면 print문이 줄바꿈 안하고 계속 출력
    print(lang1,lang2,lang3,lang4,lang5)

profile("다람쥐",20,"python","java","c","c++","c#")
profile("닭",25,"kotlin","swift","","","")



def profile_2(name, age, *language):   #여러 값을 넣어 줄떄는 *을 이용한다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end="")
    print()

profile_2("다람쥐",20,"python", "java", "c", "c++", "c#", "javaScript")
profile_2("닭",25,"kotlin", "swift", "", "", "")



# 지역변수, 전역변수---------------------------------------

# 지역변수는 함수내에서만 사용가능 함수사라지면 같이 사라짐
#전역변수는 모든곳


# gun = 10
# def checkpoint(soldiers): #근무
#     gun = gun-soldiers
#     print("[함수 내] 남은총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명 근무
# print("남은 총: {0}".format(gun))  # 오류가 나옴  gun 이라는 변수가 가장 상단에 있는 gun이 아니라 함수 내부에서 만들어진 gun이기 때문에 초기화 없이는 사용이 안된다.



gun = 10
def checkpoint(soldiers): #근무
    gun = 20 #지역 변수
    gun = gun-soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명 근무
print("남은 총: {0}".format(gun))  # 오류가 나옴  gun 이라는 변수가 가장 상단에 있는 gun이 아니라 함수 내부에서 만들어진 gun이기 때문에 초기화 없이는 사용이 안된다.

# 전체 총 : 10
# [함수 내] 남은총 : 18
# 남은 총: 10    이런 결과가 나온다.


gun = 10
def checkpoint(soldiers): #근무
    global gun # 전역 공간에 있는 gun을 사용
    gun = gun-soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명 근무
print("남은 총: {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은총 : 8
# 남은 총: 8   이런 결과가 나온다.

def checkpoint_return(gun,soldiers):
    gun = gun - soldiers
    print(" [함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총: {0}".format(gun))