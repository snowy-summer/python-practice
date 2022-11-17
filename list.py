#리스트 []
# 지하철 칸별로 10 20 30 명

subway1 =10
subway2 =20 
subway3 = 30

subway = [10,20,30] #위와 동일


subway = ["lion","tiger","pig"] #0,1,2순서
print(subway)
# pig는 몇 번쨰인가?
print(subway.index("pig")) # 0부터 세니까 2번째

#frog가 합류함
subway.append("frog")
print(subway)

#dog를 tiger과 pig사이에 합류
subway.insert(2, "dog") #(들어갈 공간, "들어가는 것") 순서 중요하다. 
print(subway)

#뒤에서 부터 빼봄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


subway.append("tiger")
print(subway)
print(subway.count("tiger")) # tiger가 몇번 들어갔는지 카운팅

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)


#다양한 자료형도 가능 

num_list = [5,4,3,2,1]
mix_list = [202,"아이",True]

print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)