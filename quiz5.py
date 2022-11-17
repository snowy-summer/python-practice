from random import*
users = range(1,21) #1~20까지 숫자 생성
users = list(users) #users의 타입을 list로 변경
shuffle (users) # shuffle은 set이 안된다.
 #sample은 리스트에서 몇개를 뽑는것


winners= sample(users,4) #4명을 뽑는다.
print("--당첨자 발표--")
print("치킨 당첨자 :{0}".format(winners[0])) 
print("커피 당첨자 :{0}".format(winners[1:]))