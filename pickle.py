#pickle


import pickle
profile_file = open("profile.pickle","wb")
profile = {"이름":"다람쥐", "나이": 20, "취미":["축구","테니스","코딩"]}
print(profile)
pickle.dump(profile,profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()


profile_file = open("profile.pickle", "rb")
profile= pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()






# with

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

#close가 필요 없다.

#with이용 파일 쓰기
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬 공부중")

#with이용 파일 읽기
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
