from random import*
class Unit:
    def __init__(self, name, hp, speed,damage): #_init_은 기본으로 쓰자
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}, 속도 : {2}\n".format(self.hp, self.damage, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현제 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도: {2}]".format(self.name,location, self.speed))
            
        
class AttackUnit(Unit): #Unit에서 상속받는다.
    def __init__(self,name,hp,speed,damage):  # self는 자기자신 의미  self를 쓰면 자기 자신에게 접근해서 값을 가지고 온다
        # self가 없을 경우는 받은 값을 그대로 가지고 온다.
        Unit.__init__(self, name, hp, speed,damage)
      #self.name = name  Unit에서 상속 받기 때문에 필요가 없어진다.
      #self.hp = hp
      #self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name ,location, self.damage))

    
class marine(AttackUnit):
    def __init__(self, name, hp, speed, damage):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

   #스팀팩: 체력 10 소모, 일정 시간  공격 속도 증가

    def stimpack(self):
     if self.hp > 10:
          self.hp-=10
          self.damage =+ 2
          print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
     else:
         print(" {0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


#탱크
class tank(AttackUnit):
 #시즈모드 : 탱크 고정 , 데미지 증가 이동 불가

 seize_devel = False


 def __init__(self, name, hp, speed, damage):
    AttackUnit.__init__(self, "탱크", 150, 1, 35)
    self.seize_mode = False
   
 def set_seize_mode(self):
     if tank.seize_devel == False:
         return
     

     #시즈모드 아닐 때 -> 시즈모드
     if self.seize_mode == False:
         print("{0} : 시즈모드로 전환합니다.".format(self.name))
         self.damage*=2
         self.seize_mode = True

     #현재 시즈모드일 때-> 시즈모드 해제
     else:
         print("{0} : 시즈모드를 해제합니다.".format(self.name))
         self.damage/=2
         self.seize_mode= False
         
       
       

        


# 드랍쉽: 수송기 공격 x

class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도: {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):  # 다중 상속
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 공중유닛은 flying_speed가 있기 때문에 speed를 0으로 해준다.
        Flyable.__init__(self, flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# #발키리 : 한번에 14발 공중공격
        
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name, "3시")

# #연산자 오버라이딩  자신 클래스에서 정의한 메소드를 사용할때

# #벌쳐: 지상유닛 빠름
# vulture = AttackUnit("벌쳐",80,10,20)

# battlecruiser = FlyableAttackUnit("배틀쿠르저",500, 25,3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name,"9시")
# battlecruiser.move("9시")
    

class wraith(FlyableAttackUnit):

    clocking_devel = False

    def __init__(self, name, hp, damage, flying_speed):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False


    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True
        
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("GG")




#게임 진행
game_start()

# 마린 3기 생성
m1= marine("마린", 40, 1, 5)
m2= marine("마린", 40, 1, 5)
m3= marine("마린", 40, 1, 5)

#탱크 2기 생성
t1 = tank("탱크", 150, 1, 35)
t2 = tank("탱크", 150, 1, 35)

#레이스 1기 생성
w1= wraith("레이스", 80, 20, 5)


#유닛 일괄 관리 (생성된 유닛 append)
atttack_units = []
atttack_units.append(m1)
atttack_units.append(m2)
atttack_units.append(m3)
atttack_units.append(t1)
atttack_units.append(t2)
atttack_units.append(w1)

#전군 이동
for unit in atttack_units:
    unit.move("1시")

#탱크 시즈모드 개발
tank.seize_devel = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (탱크: 시즈모드 레이스 : 클로킹 마린: 스팀팩)
for unit in atttack_units:
    if isinstance(unit,marine): # isinstance 지금 만들어진 객체가 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit,tank):
        unit.set_seize_mode()
    elif isinstance(unit,wraith):
        unit.clocking()

        
# 전군 공격
for unit in atttack_units:
    unit.attack("1시")

#전군피해 
for unit in atttack_units:
    unit.damaged(randint(5,21)) #데미지 5~21 랜덤으로 받음

#게임 종료
    game_over()




# 코드를 한번에 안쓰고 여러번에 걸쳐서 쓰니 잘 모르겠다. 이거는 추가적인 공부와 여러번이 필요