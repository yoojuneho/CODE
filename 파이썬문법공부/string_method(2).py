#메소드란? 클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음
letter = '코딩이 좋아요.'
print(letter)

#어떤 문자로 시작하는지 알려주는 메소드, startswith()
print("-------------어떤 문자로 시작하는지 알려주는 메소드, startswith() -------------")
print(letter.startswith('코딩이')) #불리언 값으로 출력
print(letter.startswith('딩')) #False

#어떤 값으로 끝나는지 알려주는 메소드, endswith()
print("-------------어떤 값으로 끝나는지 알려주는 메소드, endswith() -------------")
print(letter.endswith('.')) #True
print(letter.endswith('요')) #False

unnecessary = '......코..딩이 좋아요.......'
print(unnecessary)

#앞뒤로 불필요한 문자 제거, strip()
print("-------------앞뒤로 불필요한 문자 제거, strip() -------------")
print(unnecessary.strip('.')) #아무 값도 넣지 않으면 앞뒤 불필요한 공백들을 제거

#문자열 대체, replace()
print("-------------문자열 대체, replace() -------------")
print(unnecessary.replace('좋아요', '싫어요'))

#특정 값에 대한 위치, find()
print("-------------특정 값에 대한 위치, find() -------------")
print(unnecessary.find('좋아요'))

#다른 문자들 사이 가운데로, center()
print("-------------다른 문자들 사이 가운데로, center() -------------")
print(unnecessary.center(30, '-'))
print(unnecessary.center(29, '-'))