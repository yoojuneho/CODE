#if문
today = '일요일'

#if
print("-----------if-----------")
if today == '일요일':
    print('게임한판')
print('공부시작')

#if-else
print("-----------if-else-----------")
if today == '일요일':
    print('게임한판')
else:
    print('폰 5분만')
print('공부시작')

#if-elif-else
print("-----------if-elif-else-----------")
if today == '일요일':
    print('게임한판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부시작')

#-----------------if중첩-----------------

print("-----------if중첩-----------")
yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴 조심해야지')
else:
    print('주의')