#다중상속

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox, VideoMaker, MailSender): #다중상속
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

b1 = TravelBlackBox('하양이', 100000, 64)
b1.make() #상속받은 클래스의 메소드를 사용할 수 있습니다.
b1.send()
print(b1.name, b1.price)