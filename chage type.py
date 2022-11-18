#자료구조 변경

menu ={"커피","우유","밀크티"}
print(menu,type(menu)) #{'커피', '밀크티', '우유'} <class 'set'>    {} 이용했기 때문에 집합이다


#집합 -> 리스트
menu = list(menu)
print(menu,type(menu)) #['우유', '커피', '밀크티'] <class 'list'>     리스트[]


# 리스트-> 튜플
menu = tuple(menu)
print(menu,type(menu)) #('우유', '커피', '밀크티') <class 'tuple'>    튜플()


# 튜플->집합
menu =set(menu)
print(menu,type(menu)) #{'우유', '커피', '밀크티'} <class 'set'>      세트{}