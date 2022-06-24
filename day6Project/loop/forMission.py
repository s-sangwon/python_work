# forMission.py

def product_process():
    product_list = []
    for i in range(3):
        print(f'{i}번째에 기록할 제품정보를 입력하세요.')
        pno = int(input('제품번호 : '))
        pname = input('제품명 : ')
        price = int(input('가격 : '))
        tex = float(input('부가세 : '))
        amount = int(input('구매수량 : '))
        total_price = (price + price * tex) * amount
        product_list.append([pno, pname, price, tex, amount, total_price])

    for index in range(len(product_list)):
        print(f'{index}번쨰 제품정보---------------------')
        print(f'제품번호 : {product_list[index][0]}')
        print(f'제품명 : {product_list[index][1]}')
        print(f'가격 : {product_list[index][2]}')
        print(f'부가세 : {product_list[index][3]}')
        print(f'구매수량 : {product_list[index][4]}')
        print(f'구매가격 : {int(product_list[index][5])}')

if __name__ == '__main__':
    product_process()
