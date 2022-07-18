# test_matplotlib.py
# matplotlib 패키지 시각화 테스트
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# 간단한 plot(그래프) 그리기 : 기본은 선그래프임 (line plot)
# 그래프에 표현할 데이터는 리스트 또는 배열이여야 함
# 샘플 데이터 : [1,4,9,16]
def test1_plot1():
    data = [1,4,9,16]
    plt.title("Line Plot") # 그래프 제목지정 함수
    plt.plot(data) # 선그래프 만드는함수
    plt.show()

def test2_plot2():
    # title('표시할 제목') : 그래프 제목으로 설정
    # x 축 값도 함께 지정 : plot([x축값들], [y축값들])
    x_data = [10, 20, 30, 40]
    y_data = [1, 4, 9, 16]
    plt.title('x ticks')
    plt.plot(x_data,y_data)
    plt.show()

# 한글을 사용하려면, 한글폰트를 다운받아서 압출 풀어줌 ----
# matplotlib 모듈에서 기본 글꼴로 사용하게 하려면,
# matplotlib 의 위치를 확인해서 fonts/ttf 폴더 아래에
#C:\python_workspace\testVisualization\venv\lib\site-packages\matplotlib\mpl-data\matplotlibrc\fonts\ttf
# 압축푼 폰트파일을 복사해 넣음
# 예 : 나눔고딕 파일들을 복사해 넣음
# 참고 : 압축 푼 ttf 파일을 더블 클릭해서, 설치 버튼 누르고
#       설치한 경우는 windows/fonts 에 기본 설치됨
import matplotlib.font_manager as fm

def test_fonts():
    print(mpl.matplotlib_fname()) # 라이브러리 자원 저장 폴더 확인

    # 글꼴 파일 복사해 넣고 나서, matplotlib 캐시에 변경 내용 반영함
    # 1. 캐시 파일 저장 위치 확인함함
    print(mpl.get_cachedir())
    # 2. 해당위치의 캐시파일을 직접 파일탐색기에서 삭제함
    #   이전 폰트리스트 정보를 가진 캐시임
    # 3. 프로그램 다시 실행하면 캐시 파일 생김 > 확인함
    # 만약, 캐시파일 안 생기면, 컴퓨터 리부팅함


def test_fonts2():
    # 폰트 설정
    # 첫번째 방법 : rc parameter 를 설정해서 이후
    # 그래프 전체에 사용하는 방법

    # 현재 적용되고 있는 폰트 종류와 크기 확인
    print(mpl.rcParams['font.family'])
    print(mpl.rcParams['font.size'])

    # 설정 변경해 봄
    mpl.rc('font', family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    # axes 에 적용되는 유니코드에 음수 부호 설정 헤제

    # 설정 글꼴 적용 확인
    plt.title('한글 제목')
    plt.plot([10,20,30,40],[1,4,9,16])
    plt.xlabel('엑스축 라벨')
    plt.ylabel('와이축 라벨')
    plt.show()

def test_fonts3():
    # 특정 부분에서만 글꼴 설정 변경할 수도 있음
    # font_path = 'C:/resources/fonts/NanumGotic.ttf'
    font_path = 'fonts/NanumGothicBold.ttf'
    font_prop = fm.FontProperties(fname=font_path)
    plt.title('예제 그래프', fontproperties=font_prop)
    plt.plot([10,20,30,40],[1,4,9,16])
    plt.xlabel('x축 제목', fontproperties=font_prop)
    plt.ylabel('y출 제목', fontproperties=font_prop)
    plt.show()






def test_fonts4():
    # 각 객체마다 별도의 폰트 적용 : fontdict 인수에 넣어서 사용함
    #font1 ={'family' : 'C:/python_workspace/testVisualization/fonts/NanumMyeongjo', 'size': 24, 'color': 'black'}
    #font2 = {'family': '../../../../../../../fonts/NanumMyeongjoBold', 'size': 16, 'color': 'red', 'weight': 'bold'}
    font3 = {'family': 'NanumGothic', 'size': 12, 'color': 'blue', 'weight':'light'}
    #plt.title('예제 그래프', fontdict=font1)
    plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
    #plt.xlabel('x축 제목', fontdict=font2)
    plt.ylabel('y출 제목', fontdict=font3)
    plt.show()

# 그래프 만들기 설정시 스타일을 문자형 인수(argument)로 지정
def test_style():
    mpl.rc('font', family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    plt.title("'rs--' 스타일 적용 그래프")
    plt.plot([10, 20, 30, 40], [1, 4, 9, 16], 'rs--')
    plt.show()



# 스타일 지정시, 함수 매개변수의 값을 직접 지정하는 경우
def test_style2():
    plt.title("x축과 y축의 범위지정 테스트 그래프")
    plt.plot([10, 20, 30, 40], [1, 4, 9, 16],
             c='b',lw=5, ls="--",marker='o', ms=15,mec='g',mew=5, mfc='r')
    # 그래프의 범위 지정 : xlim(min,max), ylim(min,max)
    plt.xlim(0,50)
    plt.ylim(-10, 30)
    plt.show()

# 좌표 축사에 표시될 값의 위치에 대한 틱 설정
# 배열 : 같은 종류의 값 여러 개 나열 저장하는 구조의 자료형
# 리스트 : 여러 종류의 값 여러 개 나열 저장하는 구조
# 파이썬에서 배열을 다루려면 numpy 모듈을 사용함


def test_ticks():
    # 곡선 그래프 만들기
    #mpl.rc('font', family='NanumGothic')
    X = np.linspace(-np.pi, np.pi, 256)
    print('x축 값 : ',X)
    C = np.cos(X)
    print('y축 값 : ', C)
    plt.title('x축과 y축의 tick label 설정 그래프')
    plt.plot(X,C)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    plt.yticks([-1, 0, +1])
    plt.show()


# 틱라벨 문자에 LaTeX 수학식 적용가능
def test_ticks2():
    X = np.linspace(-np.pi, np.pi, 256)
    print('x축 값 : ',X)
    C = np.cos(X)
    print('y축 값 : ', C)
    plt.title('LaTeX 수학문자열로 tick label 설정 그래프')
    plt.plot(X,C)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$',
                r'$+\pi/2$', r'$+\pi$'])
    plt.yticks([-1, 0, +1], ['Low','Zero','High'])
    plt.grid(False)
    # Figure 영역에 그리드선 표시 여부 지정함수
    # True : 기본값임, False : 그리드선 표시 안함
    # Figure : 그래프가 그려지는 영역임
    plt.show()

# 선그래프의 Figure 영역에 여러 개의 선을 표시할 수 있다
# plot(x1, y1, x2, y2, x3, y3,...)
# plot(x1, y1, 'rs1', x2, y2, 'rs2',...)
def test_multlines():
    # numpy 이용 축에 사용할 데이터 만들기
    t = np.arange(0, 5, 0.2) # 0<= data < 5 0.2 간격data
    # print(t)
    plt.title('라인 플롯에서 여러개의 선 그리기')
    plt.plot(t, t, 'r--', t,
             0.5*t**2, 'bs:',
             t,0.2*t**3, 'g^-')
    plt.show()

def test_multplot():
    plt.title('복수의 plot 명령을 한 그림에서 표현')
    plt.plot([1,4,9,16],
             c='b',lw=5,ls='--', marker='o', ms='15',mec='g',mew='5', mfc='r', label='올라가')
    plt.plot([16,9,4,1],
             c='k', lw=3, ls=':', marker='s', ms=10, mec='m',mew=5,mfc='c', label='내려가')
    plt.legend(loc=2) #위치 지정하면서 범례 표시함
    plt.xlabel('x축 제목')
    plt.ylabel('y축 제목')
    plt.show()

def test_figure():
    # figure 객체 : 그래프 그림그리기 영역(종이나 캔버스), 윈도우
    # 주로 plot() 으로 생성됨
    # 그래프 창의 크기 지정 : figure(figsize=(w,h))

    # 랟넘값 발생을 위한 초기화
    np.random.seed(0) # 한번 발생한 랜덤값 계속 같은값 발생

    f1 = plt.figure(figsize=(10,2))
    plt.title('figsize=(10,2) 그래프 창 확인')
    plt.plot(np.random.randn(100)) # 1~100까지 정수 100개

    f2 = plt.gcf() # get current figure
    # 현재 사용되고 있는 figure 객체 얻어옴

    # figure 객체 생성시 할당된 객체 주소 지정됨 => 레퍼런스가 참조
    # f1, f2 는 figure 객체 참조 변수(레퍼런스) => 객체의 주소 가짐
    print(f1, id(f1))
    print(f2, id(f2))

    plt.show()

def test_axes():
    # Axes 객체 : figure  영역 안에 그려지는 그래프 그림 객체
    # x축과 y축이 포함됨 : Axis 객체
    # subplot() 을 사용하여 생성함
    # plt.subplot(행갯수, 열갯수, 순번)

    x1 = np.linspace(0., 5.)
    x2 = np.linspace(0., 2.)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)

    axes1 = plt.subplot(2, 1, 1) # 1번 Axes 객체
    plt.plot(x1, y1, 'yo-') # 1번이 Axes 에 적용되는 그래프
    plt.title('2개 그래프 표시 : 첫번째')
    plt.ylabel('Damped oscilation')

    axes2 = plt.subplot(2, 1, 2) # 2번 Axes 객체
    plt.plot(x2, y2, 'r.-')
    plt.title('2개 그래프 표시 : 두번째')
    plt.xlabel('time(sec)')
    plt.ylabel('Undamped')

    # ploy 간의 간격을 자동으로 맞출 때, tight_layout() 사용
    plt.tight_layout()
    plt.show()

def test_mult_plot():
    # 2x2 : 4개의 plot(axes객체) 을 구성
    np.random.seed(0)
    # 객체변수 = plt.subplot(행갯수, 열갯수, 순번1234)
    # plt.subplot(행열순번)

    # 2행 2열 1번째 그래프 만들기
    plt.subplot(221) # plt.subplot(2,2,1) 와 같음
    plt.plot(np.random.rand(5))
    plt.title('axes 1')

    plt.subplot(222)  # plt.subplot(2,2,1) 와 같음
    plt.plot(np.random.rand(5))
    plt.title('axes 2')

    plt.subplot(223)  # plt.subplot(2,2,1) 와 같음
    plt.plot(np.random.rand(5))
    plt.title('axes 3')

    plt.subplot(224)  # plt.subplot(2,2,1) 와 같음
    plt.plot(np.random.rand(5))
    plt.title('axes 4')

    plt.tight_layout()
    plt.show()

def test_subplots():
    # subplots() 함수로 한 번에 Axes여러개 만들기
    fig, axes= plt.subplots(2, 2)

    np.random.seed(0)

    # 첫번째 그래프 만들기
    axes[0, 0].plot(np.random.rand(5))
    axes[0, 0].set_title('axes 1')

    axes[0, 1].plot(np.random.rand(5))
    axes[0, 1].set_title('axes 2')

    axes[1, 0].plot(np.random.rand(5))
    axes[1, 0].set_title('axes 3')

    axes[1, 1].plot(np.random.rand(5))
    axes[1, 1].set_title('axes 4')

    plt.tight_layout()
    plt.show()


def test_axis():
    # Axes (그래프 : plot) 객체 안에는 축이 포함됨 : Axis 객체
    # x축과 y축 2개 이상을 Axes 가 포함함
    # 축을 여러 개 지정할 수도 있음 : twinx(), twiny() 함수 사용
    # twinx() : y축을 2개 만듦 (x축을 공유함)

    fig, axes_0 = plt.subplots() # 갯수 미지정
    axes_1 = axes_0.twinx() # x축 공유 지정

    axes_0.set_title('2개의 y축을 가진 그래프')
    axes_0.plot([10, 5, 3, 7, 1], 'r-', label='y0')
    axes_0.set_ylabel('y0')
    axes_0.grid(False)

    axes_1.set_title('2개의 y축을 가진 그래프')
    axes_1.plot([1100, 200, 300, 400, 500], 'g:', label='y1')
    axes_1.set_ylabel('y1')
    axes_1.grid(False)

    axes_0.set_xlabel('공유 x축')

    plt.show()

    # 함수 실행 테스트
if __name__ == '__main__':
    # test1_plot1()
    # test2_plot2()
    # test_fonts()
    # test_fonts2()
    # test_fonts3()
    # test_fonts4()
    # test_style()
    # test_style2()
    # test_ticks()
    mpl.rc('font', family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    # test_ticks2()
    # test_multlines()
    # test_multplot()
    # test_figure()
    # test_axes()
    # test_mult_plot()
    # test_subplots()
    test_axis()




















