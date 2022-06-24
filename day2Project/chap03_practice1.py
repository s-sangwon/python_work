# chap03_practice1
# 문자자료형 실습문제

"""
키보드로 입력받아 요구대로 처리하고 출력하시오.
"""
member_name = input('회원이름 : ')
member_id = input('회원아이디 : ')
member_passwd = input('패스워드 : ')
age = int(input('나이 : '))
height = float(input('키 : '))

passwd_slice = member_passwd[:4] + '*' * (len(member_passwd)-4)

print(f'{member_name} 회원의 아이디는 {member_id} 이고, 암호는 {passwd_slice} 입니다.')
print(f'나이는 {age}세이고, 키는 {height:0.1f}cm 입니다.')