#세트
#리스트, 튜플과 같이 값들을 저장할 수 있지만 값들의 순서가 보장되지 않고 중복 허용이 안됩니다.

A = {'돈까스', '보쌈', '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}
C = {1,2,3,4,5,6,7}

#교집합
print("----------교집합 intersection()----------")
print(A.intersection(B))

#합집합
print("----------합집합 uninon()----------")
print(A.union(B))

#차집합
print("----------차집합 difference()----------")
print(A.difference(B))

#위에서 언급했다시피 세트는 순서가 보장이 되지 않습니다. 따라서 인덱스로 접근이 불가능합니다.

#값 추가
print("----------값 추가 add()----------")
A.add('닭갈비')
print(A)

#값 제거
print("----------갑 제거 remove()----------")
B.remove('제육덮밥')
print(B)

#clear()메소드를 이용해서 모든 값을 싹 다 지울 수 있습니다.
print("----------다 제거 clear()----------")
print(C)
C.clear()
print(C) #set()으로 출력됨

#세트 완전 삭제
print("----------세트 완전 삭제 del 키워드----------")
del C
# print(C) #name 'C' is not defined라고 에러가 발생합니다.

'''
set의 기타 메소드 
copy() 세트 복사, discard() 값 삭제(해당 값이 없어도 에러 발생 X), isdisjoint() 두 세트에 겹치는 값이 없는지 여부,
issubset() 다른 세트의 부분집합인지 여부, issuperset() 다른 세트의 상위집합인지 여부, update() 다른 세트의 값들을 더함
'''
