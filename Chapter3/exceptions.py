# Exceptions (예외)

# a = 10
# b = 0
# print(a/b) # => ZeroDivisionError 발생

fruits = ['apple', 'banana', 'strawberry']
# print(fruits[3]) # => IndexError 발생

# -----------<예외를 처리하는 방법>------------

try: 
    # try 코드 안에는 오류가 발생할 가능성이 있는 코드를 작성
    print(fruits[2])
except:
    # 에러 상황을 만났을 때, 어떤 처리를 해줄 것인지 작성
    print("인덱스를 참조할 수 없습니다.")
else:
    # except(에러 상황)를 만나지 않았을 때 실행되는 코드를 작성
    print("명령 수행 완료!")

print(fruits)

# try - except 에서 예외가 발생해도 프로그램은 강제로 종료되지 않음
# => 즉! 이후 명령의 수행이 가능함




