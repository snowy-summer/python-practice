class ThailandPackage:
    def detail(self):
      print("[태국 패키지 3박 5일 ] 방콕, 파타야 여행 (야시장 투어) 50만원")

    
      
if __name__ == "__main__":
   print("직접 실행")
   print("이 문장은 직접 실행때만 나온다.")
   trip_to= ThailandPackage()
   trip_to.detail()

else:
   print(" 외부 호출")