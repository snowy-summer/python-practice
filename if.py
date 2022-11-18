weather = "비"
if weather == "비":
    print("우산을 챙기세요") #우산을 챙기세요 출력

if weather == "맑음":
    print("좋은 날씨입니다.") #weather이 맑음이 아니기 때문에 출력이 안된다.


weather = "미세먼지"
if weather == "맑음":
    print("좋은 날씨입니다.")
elif weather == "미세먼지":  # else if와 동일한 것 같다.
    print("마스크를 챙기세요")     
else :                          # 위에 있는 모든 조건이 안맞으면 실행된다.
    print("비가 올지도 모릅니다.")





weather = input("오늘 날씨는 어때요? ") # input은 입력값을받아 들인다. scanf?
if weather == "맑음":
    print("좋은 날씨입니다.")
elif weather == "미세먼지":  
    print("마스크를 챙기세요")     
else :                          
    print("비가 올지도 모릅니다.")

weather = input("날씨 어때요? ")
if weather == "비" or weather == "눈" : #비 또는 눈을 입력하면 우산을 챙기세요 출력 
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("좋아요")


temp = int(input("기온이 어때요?")) #input은 항상 문자열로 받아오기 때문에 int를 통해 숫자로 변환해줘야 한다.
if 30<= temp:
    print("더워요")
elif 10 <= temp and temp < 30:
    print("좋네요")
elif 0 <= temp < 10 : #and를 사용안해도됨
 print("쌀쌀하네요")
else: 
 print("추워요")