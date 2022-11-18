#사전형

cabinet = {3:"사자", 100:"호랑이"} #사자가 3을 할당, 호랑이가 100을 할당
print(cabinet[3]) # 사자 출력
print(cabinet[100]) #호랑이 출력

print(cabinet.get(3)) # 사자 출력
# print(cabinet[4])
# print("oh") # 5에 할당된 것이 없기 떄문에 멈추고 oh가 출력이 안됨


print(cabinet.get(4)) #get으로 불른것은 없은면 none으로 출력된다. 
#none말고 다른 것을 출력하고 싶다면
print(cabinet.get( 4,"사용가능")) # 둘이 순사가 바뀌면 , 뒤에 있는 글자가 출력이 된다.
print("oh")

print(3 in cabinet) #true     a in b    a가 b에 있는지 확인
print(5 in cabinet) #false

cabinet ={"A-3":"사자","A-100":"호랑이"}
print(cabinet)
print(cabinet["A-3"])
print(cabinet["A-100"])

#새로 딕셔너리에 추가 할 경우
print(cabinet)
cabinet["c-32"] ="펭귄"
print(cabinet["c-32"])
print(cabinet) #{'A-3': '사자', 'A-100': '호랑이', 'c-32': '펭귄'}

cabinet["A-100"]="다람쥐" # 호랑이 값에 덮어쓰기도 가능
print(cabinet) #{'A-3': '사자', 'A-100': '다람쥐', 'c-32': '펭귄'}


del cabinet["A-100"] # 삭제 del
print(cabinet) #{'A-3': '사자', 'c-32': '펭귄'}

#key 들만 출력
print(cabinet.keys()) #a-3, c-32 출력

#value만 출력
print(cabinet.values())# 사자, 펭귄 출력
print(cabinet.values()) #dict_values(['사자', '펭귄'])

#둘다 출력
print(cabinet.items()) #dict_items([('A-3', '사자'), ('c-32', '펭귄')])

#딕셔너리 비우기
cabinet.clear()
print(cabinet) #{} 출력됨