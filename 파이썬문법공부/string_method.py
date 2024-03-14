letter = "how are YOU?"
print(letter)

#모두 소문자로 만들기, lower()
print("--------모두 소문자로 만들기 lower() --------")
print(letter.lower())

#모두 대문자로 만들기, upper()
print("--------모두 대문자로 만들기 upper() --------")
print(letter.upper())

#첫 글자만 대문자로 만들기, capitalize()
print("--------첫 글자만 대문자로 만들기 capitalize() --------")
print(letter.capitalize())

#각 단어들의 첫 글자만 대문자로 만들기, title()
print("--------각 단어들의 첫 글자만 대문자로 만들기, title() --------")
print(letter.title())

#대문자와 소문자 바꾸기, swapcase()
print("--------대문자와 소문자 바꾸기, swapcase() --------")
print(letter.swapcase())

#문자열 나누기, split() 띄어쓰기를 기준으로 단어를 나눈 후 리스트로 만들어서 출력
print("--------문자열 나누기, split() --------")
print(letter.split())

#문자열 내에서 특정 문자가 얼마나 많이 사용되었는지, count()
print("--------문자열 내에서 특정 문자가 얼마나 많이 사용되었는지, count() --------")
print(letter.count('how'), '-> how가 얼마나 많이 쓰였는지?')
print(letter.count('o'), '-> o가 얼마나 많이 쓰였는지? **소문자 대문자 구분됨**')