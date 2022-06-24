# fileio_mission.py
# 파일입출력, 반복문, 리스트, 딕셔너리 사용 실습 문제

import pickle
import os

def emp_process():
    emp_dict = dict()
    emp_list = list()
    prompt = '''
    *** 직원 정보 관리 프로그램 시작 ***
    1. 새 직원정보 추가
    2. 직원정보 삭제
    3. 전체 출력
    4. 파일에 저장
    5. 파일로 부터 직원정보 읽어오기
    9. 프로그램 끝내기
    '''

    while True:
        print(prompt)

        no = int(input('번호 입력 : '))

        if no == 1:

            empid = input('사번 : ')
            empname = input('이름 : ')
            empno = input('주민번호 : ')
            email = input('이메일 : ')
            phone = input('전화번호 : ')
            salary = int(input('급여 : '))
            job = input('직급 : ')
            dept = input('부서 : ')
            emp_list.append([empid, empname, empno, email, phone, salary, job, dept])
            emp_dict.update({empid: emp_list[-1]})
            #emp_dict[empid] = [empid, empname, empno, email, phone, salary, job, dept]
            print(empid + '번 사번의 직원 정보가 입력되었습니다.')

            print('직원 정보를 올바르게 입력해주세요.')
        elif no == 2:

            delpid = input('삭제할 사번 : ')
            emp_dict.pop(delpid)
            print(delpid+'번 사번의 직원 정보가 삭제되었습니다.')

        elif no == 3:
            for eno in emp_dict:
                print(f'{eno} : {emp_dict.get(eno)}')

        elif no == 4:
            fname = input('저장할 파일명 : ')
            f = open(fname, 'wb')
            pickle.dump(emp_dict, f)
            f.close()
            print(f'{fname} 파일에 성곡적으로 저장되었습니다.')
        elif no == 5:
            fname = input('읽을 파일명 : ')
            f = open(fname, 'rb')
            emp_dict = pickle.load(f)
            f.close()
            print(emp_dict)
        elif no == 9:
            break
        else:
            print('유효한 번호를 입력하세요.')
    print('직원 관리 프로그램이 종료되었습니다')

def emp_process2():
    emp_dict = dict()
    emp_list = list()
    prompt = '''
    *** 직원 정보 관리 프로그램 시작 ***
    1. 새 직원정보 추가
    2. 직원정보 삭제
    3. 전체 출력
    4. 파일에 저장
    5. 파일로 부터 직원정보 읽어오기
    9. 프로그램 끝내기
    '''

    while True:
        print(prompt)
        try:
            no = int(input('번호 입력 : '))
        except:
            print('유효한 번호를 입력하세요.')
            continue
        if no == 1:
            try:
                empid = input('사번 : ')
                empname = input('이름 : ')
                empno = input('주민번호 : ')
                email = input('이메일 : ')
                phone = input('전화번호 : ')
                salary = int(input('급여 : '))
                job = input('직급 : ')
                dept = input('부서 : ')
                emp_list.append([empid, empname, empno, email, phone, salary, job, dept])
                emp_dict.update({empid: emp_list[-1]})
                print(empid + '번 사번의 직원 정보가 입력되었습니다.')
            except:
                print('직원 정보를 올바르게 입력해주세요.')
        elif no == 2:
            try:
                delpid = input('삭제할 사번 : ')
                emp_dict.pop(delpid)
                print(delpid+'번 사번의 직원 정보가 삭제되었습니다.')
            except:
                print('유효한 사번을 입력하세요.')
                continue
        elif no == 3:
            for eno in emp_dict:
                print(f'{eno} : {emp_dict.get(eno)}')
        elif no == 4:
            f = open('employees.dat', 'wb')
            pickle.dump(emp_dict, f)
            f.close()
            print('employees.dat 파일에 성곡적으로 저장되었습니다.')
        elif no == 5:
            f = open('employees.dat', 'rb')
            emp_dict = pickle.load(f)
            f.close()
            print(emp_dict)
        elif no == 9:
            break
        else:
            print('유효한 번호를 입력하세요.')