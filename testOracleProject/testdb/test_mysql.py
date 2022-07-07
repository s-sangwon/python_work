# test_mysql.py

# 파이썬 외부 모듈 설치와 사용
# 파이썬 외부 모듈은 프로젝트에 설치해야 함
# 파이참에서 외부 패키지 모듈 설치하는 방법이 3가지 있음
# 방법 1 :
# 파이참 틀 아래쪽의 'Python Packages' 탭 클릭
# > 해당 뷰가 아래쪽에 표시됨,
# > 설치하고 싶은 패키지명 입력해서 설치하면됨.
# > 검색영역에 설치할 패키지명을 입력
# > 검색되면 패키지명 클릭 > 오른쪽에 클릭한 패키지 정보가 표시됨 > 오른쪽위에 install 클릭
# > 성공적으로 설치됨 메세지 확인하고, 설치 버전 확인함

# 방법 2 : 모든 파이썬 개발툴에서 공통으로 사용하는 방법임
# Terminal 터미널 탭 클릭
# > 현재 프로젝트 경로명> 프롬프트 표시됨
# > 프롬프트에서 설치 명령어를 직접 입력해서 설치함
# > pip install 설치할패키지명
# 주의사항 : pip 버전을 먼저 upgrade 해야함
# pip 가 이미 설치되어 있다면 upgrade
# 패키지 설치와 pip 업그레이드 동시 수행할 수 있음
# > python -m pip install --upgrade 설치할패키지명

# 방법 3 :
# File 메뉴 > settings...(설정) > Project : 프로젝트명 표시 찾음
# > 프로젝트명 부분을 확장시킴
# > 우측 또는 아래쪽의 'python interpreter' (python 인터프리터)
# > 서택 > 오른쪽의 설치된 패키지(모듈) 목록을 볼 수 잇음
# > 위의 '+' 클릭 > 새 창 열림
# 설치할 패키지 검색 > 모듈이름 선택 > 아래쪽의 '설치' 버튼 클릭
# 설치 성공 메세지 확인하고 창 닫음

# 데이터베이스 연동에 필요한 파이썬 패키지 -------------
# mysql db : pymysql 필요
# oracle db : cx-Oracle 필요

# 1. 설치 후에 improt 선언하고 사용함
import pymysql,cx_Oracle

# 2. 해당 데이터베이스에 연결하기 위한 코드 작성
# db 서버의 ip주소(url), port 번호, 사용자계정과 암호

dbURL = "localhost" # db server ip 주소 예 : "192.168.120.34"
dbPORT = 3306
dbUSER = "root"
dbPASSWORD = "1234"

#데이터베이스 연결
# 임포트한 모듈에서 메소드를 제공함 : pymysql.connect()
conn = pymysql.connect(host=dbURL, prot=dbPORT, user=dbUSER, passwd=dbPASSWORD,
                       db="test", charset="utf-8", use_unicode=True)
# 연결이 실패하면 conn = null
# conn != null 이면 연결 성공임.

# db 연결이 성공했다면, 필요한 쿼리문(select, insert, update, delete)
#을 작성하고 db로 보내서 실행되게 하고 결과를 받음
# C(Create : insert문),
# R(Read : select 문),
# U(Update : Update 문),
# D(Delete : delete문)

#예 : select 쿼리문 작성해서 실행 처리
query = 'select * from test.sample'

cursor = conn.cursor()  # db 로 보내서 실행할 객체
cursor.execute(query) # 쿼리문 보내서 실행
result = cursor.fetchall() # 조회된 모든 결과를 받음
print(result)
print(type(result)) # tuple

# 4. 쿼리문이 dml 구문이면 트랜잭션 처리 필수임
if result > 0:
    conn.commit()
else:
    conn.rollback()


# db 사용이 끝나면
conn.close()
