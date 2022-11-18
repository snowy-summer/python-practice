#튜플 (리스트보다 빠르다)

menu =("돈까스","치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

#튜플 추가 하는법

name = "사자"
age =20
hobby = "달리기"

print(name,age,hobby)

(name,age, hobby) = ("사자", 20, "달리기")
print(name,age,hobby)

name,age, hobby = "사", 20, "달기" #괄호를 안해도 가능하다.
print(name,age,hobby)