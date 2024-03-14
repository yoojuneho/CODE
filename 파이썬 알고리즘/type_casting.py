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
