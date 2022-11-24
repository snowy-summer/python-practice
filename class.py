
class Unit:
    def __init__(self, name, hp, speed,damage): #_init_은 기본으로 쓰자
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력: {0}, 공격력: {1}\n".format(self.hp, self.damage))

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

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현제 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛이 파괴되었습니다.".format(self.name))



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

#발키리 : 한번에 14발 공중공격
        
valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name, "3시")

#연산자 오버라이딩  자신 클래스에서 정의한 메소드를 사용할때

#벌쳐: 지상유닛 빠름
vulture = AttackUnit("벌쳐",80,10,20)

battlecruiser = FlyableAttackUnit("배틀쿠르저",500, 25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")
    

#건물

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp, 0)
        super().__init__(name,hp,0) # super는 괄호와 쓰고 self를 안써도 된다.
        self.location = location



