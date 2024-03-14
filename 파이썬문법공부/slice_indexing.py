lang = 'python'
print(lang[0], '파이썬은 0부터 인덱스가 시작')
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])
print(lang[5])

print("----------------거꾸로하면 ~ -1 까지----------------")

print(lang[-6])
print(lang[-5])
print(lang[-4])
print(lang[-3])
print(lang[-2])
print(lang[-1])

#---------------------------슬라이싱---------------------------
print("----------------슬라이싱----------------")

print(lang[0:1], '-> [0:1] 처음과 끝을 지정')
print(lang[:2], '-> [:2] 끝만 지정')
print(lang[1:], '-> [1:] 처음만 지정')
print(lang[:], '-> [:] 전체 선택')