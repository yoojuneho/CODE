import StudyPackage.goodjob
StudyPackage.goodjob.say()

from StudyPackage import goodbye
goodbye.bye()

#두개 모듈을 다 쓰고 싶은 경우
from StudyPackage import goodbye, goodjob
goodjob.say()
goodbye.bye()