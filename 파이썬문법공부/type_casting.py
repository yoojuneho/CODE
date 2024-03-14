a = '3.5'
b = '2'
c = 3.5
d = 2

to_int = int(b)
to_int2 = int(float(a)) # 먼저 float로 바꾼 후 int로 바꿔야 함, 정수로 바뀔때 소수점 부분은 없어진다.
to_float = float(a)
to_float2 = float(b)
to_str = str(c)
to_str2 = str(d)

print(to_int, to_int2, to_float, to_float2, to_str, to_str2)

#----------------------------------------------------------------------------------------------#
aa = 'hello'
bb = '     '
cc = ''

print("--------------문자열에 대한 불리안 값들--------------")
#불리안의 True, False 기준은 값이 있고 없고의 차이
print(bool(aa)) 
print(bool(bb))
print(bool(cc), "-> 문자열의 경우 비어있으면 값이 없는 걸로 판단") #문자열의 경우 변수 cc만 값이 없는 것으로 나옴

print("--------------숫자에 대한 불리안 값들--------------")
print(bool(-1))
print(bool(1))
print(bool(0), "-> 숫자의 경우 0은 값이 없는 걸로 판단") #숫자의 경우 0만 값이 없는 걸로 판단

print("--------------그 외--------------")
print(bool(None))