#클래스
#여러 변수들을 묶어서 한 번에 관리할 수도 있고, 클래스 안에 어떤 기능을 하는 함수를 만들어 넣을 수도 있습니다.
'''
class 클래스명:
    정의
'''

class BlackBox:
    #pass #파이썬에서 pass를 사용함으로써 구현을 미룰 수 있습니다.
    def __init__(self, name, price): #인스턴스를 초기화 해주는 함수입니다.
        self.name = name
        self.price = price

    def set_travel_mode(self): #메소드
        print("여행 모드 ON")

b1 = BlackBox('까망이', 200000) #b1객체 생성
b1.set_travel_mode()
print(b1.name, b1.price) #클래스 객체의 변수에 접근하기 위해서 점(.)을 사용합니다.
print(isinstance(b1, BlackBox)) #b1객체가 BackBox의 인스턴스인지 확인하는 함수입니다.

#self는 '객체 자기 자신'을 의미합니다.
'''
1. 메소드를 정의할 때 처음 전달값은 반드시 self
2. 메소드 내에서는 self.name과 같은 형태로 멤버변수를 사용
'''