#for
'''
for 변수 in 반복 또는 대상:
   반복 수행 문장
'''

for x in range(10): # range()는 어떤 범위 내의 숫자들을 만들어주는 역할을 합니다. range(10) : 0 ~ 9
    print('팔 벌려 뛰기 해')

#f-string 방법을 이용한 반복문

for x in range(1,10,2):
    print(f'팔 벌려 뛰기 {x}회')