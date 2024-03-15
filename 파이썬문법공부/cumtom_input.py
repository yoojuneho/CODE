#사용자 입력
#input()로 입력받은 값은 문자열입니다.

name = input("예약자분 성함이 어떻게 되나요?")
print(name)

num = input("총 몇 분이세요?")
if int(num) > 4: #int로 타입 캐스팅을 해야합니다.
    print("사람이 많네요.") 