#사전
#key값과 value값이 항상 쌍으로 이루어며 이때 key는 중복이 허용되지 않습니다.
#딕셔너리 = {key1:value1, key2:value2, ... } key와  value가 콜론(:)으로 구분합니다.

person = {
    '이름': '유준호',
    '나이': 25,
    '키': 180,
    '몸무게': 75
}

'''
위와 같은 코드형식으로 표현할 수 있으며, key값은 문자열, 숫자 등 다른 형태로도 정의할 수 있습니다. (중복만 피하면 됩니다.)
value값도 숫자, 문자, 불리안, 리스트나 튜플 등도 얼마든지 사용할 수 있습니다.
'''

print(person['이름'])
print(person['나이'])
print(person.get('별명')) # 없는 key에 접근하면 None이 출력됩니다.

print("----------새로운 key값 추가하기----------")
person['주소'] = '인천시' # 새로운 데이터를 추가하는 방법
print(person['주소'])

print("----------value값 변경하기----------")
person['키'] = 190 # 키 값 변경하기
print(person['키'])

#update()
print("----------여러 value값들을 바꾸고 싶을 때----------")
person.update({'키':185, '몸무게':73})
print(person)

#pop()
print("----------특정 key값 삭제하기")
person.pop('몸무게')
print(person)

#keys()
print("----------어떤 key값들이 있는지 확인할 때 keys()----------")
print(person.keys())

#values()
print("----------어떤 value값들이 있는지 확인할 때 values()----------")
print(person.values())

#어떤 key:value 들이 있는지?
print("----------key와 value로 구분된 모든 데이터 확인 items()----------")
print(person.items())

#clear()
print("----------모든 데이터 삭제 clear()----------")
person.clear()
print(person)

'''
dictionary의 기타 메소드
fromkeys() 제공된 keys를 통해 새로운 딕셔너리 생성 및 반환, popitem() 마지막으로 추가된 데이터 삭제
setdefault() key에 대항하는 value 반환, key가 없다면 새로 만들고 default value 설정 및 반환
'''