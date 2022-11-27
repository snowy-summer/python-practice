class Unit:
    def __init__(self):
        print(" unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        super().__init__()  #super는 다중 상속일 경우 맨 마지막에 상속받는 것이 안됨
        (self)


#드랍쉽

dropship = FlyableUnit()    # 