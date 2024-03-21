# TTS (Text To Speech)
# STT (Speech To Text) 

from gtts import gTTS # 컴퓨터 음성으로 바꾸기 위해서 텍스트를 정의해야함 gTTS를 이용해서 텍스트를 음성으로 바꿈. 바꾼 후 MP3형태같은 걸로 저장
from playsound import playsound #playsound패키지를 통해서 파일을 열어서 실행하는 것이 아니라 바로 실행 가능

file_name = 'sample.mp3'

# 영어 문장
# text = 'Situated in Carle Place, 6.4 km from Nassau Veterans Memorial Coliseum, parking'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name) # sample.mp3를 파일로 저장
# playsound(file_name) # mp3 파일 재생

# 한글 문장
text = '파이썬을 배우면 이런 것도 할 수 있어요'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name) # mp3 파일 재생