# 오라클 연동과 수업용 계정 employee 테이블 CRUD 처리 프로젝트

# 패키지 설명
# common 패키지 : 여러 패키지들이 공통으로 사용할 파이썬 코드파일
#               오라클 드라이브 등록, 오라클 연결, commit/rollback, close
# employee 패키지 : 수업용계정의 employee 테이블 CRUD 처리 코드 파일
# department 패키지 : 수업용계정의 department 테이블 CRUD 처리 코드 파일

import common.oracle_db as oradb
import menu





if __name__ == '__main__':
    # 프로젝트 실행시 오라클 드라이브 등록 설정 실행
    oradb.oracle_init()
    menu.display()
