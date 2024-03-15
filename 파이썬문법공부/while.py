#while
#조건이 참인 동안 계속해서 반복합니다.
'''
while 조건:
    반복 수행 문장
'''

max = 25
weight = 0
item = 3

while weight + item <= max:
    weight += item
    print('짐을 추가합니다.')
print(f'총 무게는 {weight}입니다.')

#break
drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        break
    print(f'{x} 시청')

#continue
for x in drama:
    if x == '시즌3':
        print('재미 없대, 건너 뛰자')
        continue
    print(f'{x} 시청')