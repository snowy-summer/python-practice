absent = [2,5] #결석 가정
for student in range(1,11):
    if student in absent:  # student가 absent안에 있다면 continue를 실행
        continue           # continue는 밑문장을 실행하지 않고 다음 반복으로
    print("{0} 책읽어봐".format(student))



absent = [2,5] #결석 가정
no_book = [7] #책없음
for student in range(1,11):
    if student in absent:   #2,5 일때만 true라 continue실행
        continue
    elif student in no_book: #7일때만 true라 밑 문장과 break로 중단
        print("오늘 수업끝{0}따라와".format(student))
        break  
    print("{0} 책읽어봐".format(student))
# continue는 다음 반복으로 넘어간다.
#break는 반복문이 중단된다.