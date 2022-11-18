#집합 (set)
#중복안됨, 순서 없음
my_set ={1,2,3,3,3}
print(my_set) # 1,2,3 만 출력됨

java = {"일호","이호","삼호"}
python = set(["일호","사호"]) #리스트 형식 만들고 그위에 만듬

#교집합
print(java & python) #일호 출력
print(java.intersection(python)) #일호 출력

#합집합
print(java | python) #{'삼호', '이호', '일호', '사호'} 출력 순서가 없다
print(java.union(python))

#차집합 

print(java-python) #{'삼호', '이호'} 출력
print(java.difference(python))


#추가하기
python.add("오호")
print(python) #{'일호', '사호', '오호'}

#빼기
java.remove("일호")
print(java) #{'삼호', '이호'