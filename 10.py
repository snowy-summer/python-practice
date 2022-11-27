# 예외 처리 

try:

    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append  (int(input("첫 번째 숫자를 입력하세요 :")))
    nums.append  (int(input("두 번째 숫자를 입력하세요 :")))
    nums.append  (int(nums[0]/nums[1]))
    print("{0} / {1} = {2} ".format(nums[0], nums[1] , nums[2]))
except ValueError:                            #ValueError 가 발생하면 처리 해준다.
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err) # 에러 문구를 그대로
# except:
#     print(" 알 수 없는 에러가 발생하였습니다.")  # 위의 두 에러를 제외한 모든 에러가 처리 가능함

except Exception as err:                            # 어떤 에러가 발생했는지 알 수 있다.
    print(" 알 수 없는 에러가 발생하였습니다.")
    print(err)






#에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise ValueError                                #raise가 에러를 그냥 발생시킨다.
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")


    
#사용자 정의 에러 발생시키기
class BigNumberError(Exception):
    def _init_(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise BigNumberError("입력값: {0},{1} ".format(num1,num2))
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
    print(err)



#finally

finally:                                        #마지막에 에러가 나오던 말던 무조건 실행 
    print(" 계산기를 이용해 주셔서 감사합니다.")
