#예외처리
'''
try: (필수)
    수행문장
except: 
    에러 발생 시 수행 문장 -> 에러 상황이 발생했을 때만 수행할 문장
else: 
    정상 동작 시 수행 문장 -> 에러가 발생하지 않았을 때만 수행할 문장
finally:
    마지막으로 수행할 문장 -> 에러 여부 상관 없이 항상 수행되는 문장

<에러처리 form>
try:            try:             try:           try:
ecxept:   or    finally:   or    except:   or   except:
                                 else:          else:
                                                finally:
'''

try:
    num1 = 3
    num2 = 0
    result = num1 / num2 
    print(f'연산 결과는 {result}입니다.')
except:
    print('에러가 발생했어요.')
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')