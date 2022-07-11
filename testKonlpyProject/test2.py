# test2.py
# konlpy 모듈에서 Okt 클래스 매개변수 테스트 : Okt 클래스 사용
from konlpy.tag import Okt
from konlpy.utils import read_txt
#import tweepy
import jpype

# 형태서 분석 태깅 : pos(), morphs(). nouns()
# norm 형태소를 깔끔하게 만들어 주고, 불필요한 데이터를 지움
# stem 형태소의 원형을 찾아서 반환해 줌
okt = Okt()
text = read_txt('sample.txt', u'utf-8')

print('norm=True, stem=True')
malist = okt.pos(text, norm=True, stem=True)
print(malist)

print('norm=False, stem=False')
malist = okt.pos(text, norm=False, stem=False)
print(malist)

print('norm=False, stem=True')
malist = okt.pos(text, norm=False, stem=True)
print(malist)

print('norm=True, stem=False')
malist = okt.pos(text, norm=True, stem=False)
print(malist)