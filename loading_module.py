# import module
# module.price(3) #3명 이서 영화 보러 갔을 때 가격
# module.price_morning(3) #조조 3
# module.price_solider(3) # 솔저 3


import module as mv # module를 mv로 줄여서 사용가능
mv.price(3)
mv.price_morning(3)
mv.price_solider(3)



from module import * #모듈 이름 안써도 됨 from random import* 이랑 같음
price_solider(3)
price(3)
price_morning(3)

from module import price,price_morning   #price,price_morning 만 불러오기
price(3)
price_morning(3)

from module import price_solider as price  #
price(5)