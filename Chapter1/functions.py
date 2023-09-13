# 함수(Functions) 
# 매개변수(파라미터), 인자(인수)

# 'name' => 매개변수(파라미터)
# => 함수를 정의하는 곳에 쓰이는 변수같은 개념
# def print_name(name):
#     print(f'이름은 {name} 입니다')

# 입력받은 이름, "김땡땡" => 인자(인수)
# => 함수를 실행할 때 넘겨주는 값은 인자(인수) 라고 함
# print_name(input("이름을 입력하세요:"))
# print_name("김땡땡")

# def print_ex_string():
#     print('예시 문자열 입니다')
# print_ex_string()

# def print_name_age(name, age):
#     print(f'이름은 {name} 이고, 나이는 {age} 입니다.')
# print_name_age("김해김씨", "24")



# def order_coffee(qty, option='hot'): # 고정되어 있는 옵션인 'hot'
    # 기본값이 없는 파라미터 이후에 지정할 인자의 값을 작성해야 함.
    # qty, option='hot' 순서를 바꿔서 작성한다면 오류가 남
    # print(f'{qty}잔 / {option}')

# order_coffee(3, 'iced')
# order_coffee(2) # option은 hot 으로 자동생성됨
# order_coffee(option='iced', qty=1) # qty 값을 직접 줌
# => 이 경우에는 순서가 바뀌어도 괜찮음.



# def get_id(email):
    
#     if email.endswith('@test.com'): # 어떠한 문자열로 끝나는지 판결
#         email_id = email.removesuffix('@test.com')
        # @test.com 삭제한 email 을 email_id 변수에 할당
        # print(email_id)
        # return email_id # 반환받고 싶은 변수 써놓음
        # 만약 return 부분이 없다면, user_id 부분에는 Null 값이 생김
        # => get_id 함수를 실행하고 반환할 데이터가 휘발되기 때문
#     else:
#         print('처리할 수 없는 이메일 주소!')

# user_id = get_id(input("이메일을 입력해주세요: "))
# print(f'이메일 아이디는 {user_id} 이군요!')


# ---------< 모듈(module) 사용 >----------

from id_getter import get_id
# from (모듈의_이름) import (함수의_이름)

get_id('test1@test.com')

user_id = get_id(input("이메일을 입력해주세요: "))


