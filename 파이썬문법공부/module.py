import for_module # 모듈을 통째로 가져왔습니다.

for_module.say() # 때문에 가져온 모듈에서 say()메소드를 쓰기 위해선 for_module.say()와 같이 작성해야 합니다.

#from 모듈 import 변수, 함수 또는 클래스
from for_module import say # 모듈에서 하나의 함수만 쓸 것 같다 싶을 때 이와같이 작성하면 say()메소드만 코드로 작성하면 됩니다.
say()

#EX)
import random
my_list = ['가위', '바위', '보']
print(random.choice(my_list))