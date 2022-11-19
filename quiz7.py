def std_weight (height,gender):
    global man
    if "남자" in gender:
        weight = (height/100)*(height/100)*22
    else:
        weight = (height/100)*(height/100)*21
    print("키 {0} {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))
    return weight,height,gender

std_weight(175,"남자")
std_weight(175,"여자")




# 답
def std_weight (height,gender): #키 m단위 실수 , 성별 :남,여
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 #cm단위
gender = "남자"
weight = round(std_weight(height / 100, gender),2)


print("키 {0} {1}의 표준 체중은 {2}kg입니다.".format(height,gender,weight))