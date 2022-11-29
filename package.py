import travel.thailand #import 할 때 모듈이나 패키지만 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()



from travel import *  # 이 상태에서는 베트남이 안불러와진다.  추가적인 범위 설정이 필요
trip_to = vietnam.VietnamPackage()
trip_to.detail()

