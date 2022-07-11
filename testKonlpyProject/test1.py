# test1.py
# 한글 형태소 분석 테스트1 스크립트

# Hannanum - KAIST 말뭉치를 이용해 생성된 사전
from konlpy.tag import Hannanum # 클래스만 임포트함
from konlpy.tag import Kkma
from konlpy.tag import Komoran


hannanum = Hannanum() # 레퍼럿느변수 = 객체생성()

print('hannanum ------------------------------------')
text1 = u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'
#에러 발생 : [ImportError: DLL load failed: 지정된 모듈을 찾을 수 없습니다.] 아래 링크 설치로 해결
#https://www.microsoft.com/ko-kr/download/details.aspx?id=48145
print(hannanum.analyze(text1))
print(hannanum.nouns(text1))
print(hannanum.pos(text1))

# Kkma - 세종 말뭉치를 이용해 생성된 사전 (꼬꼬마)
from konlpy.tag import Kkma
kkma = Kkma()

# 메소드 정리
# Kkma.sentences() # 문장 분석
# Kkma.morphs() # 형태소분석
# Kkma.nouns() # 명사 분석
# Kkma.pos() #


print('Kkma ------------------------------------')
print(kkma.morphs(text1))
print(kkma.nouns(text1))
print(kkma.pos(text1))
print(kkma.sentences(text1))


from konlpy.tag import Komoran

komoran = Komoran()

# 메소드 정리

# Kkma.morphs() # 형태소분석
# Kkma.nouns() # 명사 분석
# Kkma.pos() # 형태소 분석 태깅

print('komoran ------------------------------------')
print(komoran.morphs(text1))
print(komoran.nouns(text1))
print(komoran.pos(text1))

from konlpy.tag import Okt

okt = Okt()
# 메소드 정리

# okt.morphs() # 형태소분석
# Kkma.nouns() # 명사 분석
# Kkma.pos() # 형태소 분석 태깅

print('okt ------------------------------------')

print(okt.nouns(text1))
print(okt.pos(text1))
print(okt.morphs(text1, stem= True))
print(okt.morphs(text1)) # stem : 각 단어에서 어간 추출 처리 매개변수