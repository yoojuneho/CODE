#함수? 어떤 동작을 수행하는 코드들의 묶음을 말합니다.
#여러 곳에서 사용되는 코드는 하나의 함수로 만들면 굉장히 편리합니다.
'''
def 함수명():
    수행할 문장
    return 반환값
'''

#매개변수를 활용한 함수
def cut_price(x):
    print(f'{x}님 커트 가격은 15000 원입니다.')

cut_price('유준호')

#반환값을 활용한 함수
#함수에서 반환 값은 보통 한개지만, 필요하면 튜플 형태로 여러 개의 값들을 반환 할 수 있습니다.
#반환되는 즉시 함수 탈출하게 됩니다.
#기본 값, 기본 파라미터 값
'''
def 함수명(전달값=기본값):
    수행할 문장
'''
#단골 손님에 대한 가격 할인???
def get_price(is_vip=False):
    if is_vip == True:
        return 10000
    else:
        return 15000
    
vip_price = get_price(True)
print(f'단골 손님의 커트 가격은 {vip_price}입니다.')
normal_price = get_price()
print(f'일반 손님의 커트 가격은 {normal_price}입니다.')

#키워드 값, 여러개의 파마미터 값을 기본값으로 설정할 때 어떤 기본값을 사용하는지에 관한 방법입니다.
def order(shot=2, size='Regular', takeout=True):
    print(f'아메리카노 {size}사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다.')
    else:
        print('주문이 완료되었습니다.')

order(1,'Venti', True)