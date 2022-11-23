name = "마린"
hp = 40
damage = 5
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0},  공격력 {1}\n".format(tank_hp,tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( name,location, damage))

attack(name, "1 시", damage)
attack(tank_name, "1시", tank_damage)   

# 유닛이 한마리면 상관이 없는데 몇백마리면 힘들기 때문에 Class를 사용한다.

class Unit:
    def __init__(self, name, hp, damage): #_init_은 기본으로 쓰자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))


wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True  # Unit에클로킹이라는 변수가 없는데 외부에서 추가로 생성 가능해서 붙혀 넣기가 가능하다.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))






class AttackUnit(Unit): #Unit에서 상속받는다.
    def __init__(self,name,hp,damage):  # self는 자기자신 의미  self를 쓰면 자기 자신에게 접근해서 값을 가지고 온다
        # self가 없을 경우는 받은 값을 그대로 가지고 온다.
        Unit.__init__(self, name, hp,damage)
      #self.name = name  Unit에서 상속 받기 때문에 필요가 없어진다.
      #self.hp = hp
      #self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name ,location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현제 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃",50,16) # 파이어뱃 생성
firebat1.attack("5시") # 5시 방향으로 공격
firebat1.damaged(25) # 25데미지 입음
firebat1.damaged(25) #25데미지 입고 체력 0 으로 파괴
