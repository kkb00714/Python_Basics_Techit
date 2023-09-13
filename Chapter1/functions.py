# 함수(Functions) 
# 매개변수(파라미터), 인자(인수)

# 'name' => 매개변수(파라미터)
# => 함수를 정의하는 곳에 쓰이는 변수같은 개념
def print_name(name):
    print(f'이름은 {name} 입니다')

# 입력받은 이름, "김땡땡" => 인자(인수)
# => 함수를 실행할 때 넘겨주는 값은 인자(인수) 라고 함
# print_name(input("이름을 입력하세요:"))
# print_name("김땡땡")

# def print_ex_string():
#     print('예시 문자열 입니다')
# print_ex_string()

def print_name_age(name, age):
    print(f'이름은 {name} 이고, 나이는 {age} 입니다.')
print_name_age("김해김씨", "24")