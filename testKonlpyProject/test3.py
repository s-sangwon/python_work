# test3.py
# 공공데이터포털 에서 csv 파일 다운받기
# csv 파일 읽어들이기
# 읽어들인 데이터에서 가장 많이 사용된 명사 찾기

import codecs
import csv
from konlpy.tag import Okt



okt = Okt()
word_dic = {} # dictionary
lines = [] # list

# 파일변수 = open('파일명.확장자', '열기모드')
# 파일변수.read(), 파일변수.write()
# 처리가 완료되면. 반드시 파일변수.close()

# csv 파일에서 데이터를 읽어온다. : codecs 모듈 제공 함수
# 파일 입출력이 끝나면 자동 close 처리함 : with resource 문

with open('testcsv.csv', 'r') as raws:
    reader = csv.reader((raws))
    for raw in reader:
        lines.append(raw) # 파일에서 읽은 한줄씩 데이터 리스트에 저장
# 저장구조 : [[],[],[],[],[],[],...]

for line in lines:
    malist = okt.pos(' '.join(line))
    #print('mal',malist)

    # 명사들을 수집해서 반복되는 명사 count 를 진행
    for word in malist:
        if word[1] == "Noun": # [단어, 태그]
            if not(word[0] in word_dic):
                # 해당 단어가 사전에 저장되어 있지 않다면
                word_dic[word[0]] = 0 # 단어 : 0 => 저장
                # 딕셔너리는 저장안 된 키에 값 대입하면 자동 저 됨.
            word_dic[word[0]] += 1 # 단어(키)의 값 1증가
data = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)

# 50개까지 결과값을 출력
print('keys')
print(data)

print('result')
for word, count in data[:50]:
    print("{0}({1})".format(word, count), end=", ")


# wordcloud 만들기
# wordcloud 패키지 설치하고 사용함 -> matplotlib 자동 설치
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import  Image
import numpy as np

img = Image.open('heart.png') # 이미지 오픈
imgArrary = np.array(img) # 이미지의 각 픽셀을 수치로 변환
print(imgArrary)
# wordcloud = WordCloud( \
#             font_path='malgun.ttf', \
#             background_color = 'white', \
#             width = 1000, height = 800)\
#     .generate_from_frequencies(dict(data))
#
# plt.figure(figsize=(10,10))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

wordcloud = WordCloud(
            font_path='malgun.ttf',
            background_color = 'white',
            width = 400, height = 400,
            max_font_size = 100,  # 빈도수가 가장 큰 글자의 크기 지정
            mask = imgArrary).generate_from_frequencies(dict(data))

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()