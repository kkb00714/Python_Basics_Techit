# 회원가입을 구현해보자! 

print('==============================\n')
print('회원가입\n')
print('==============================\n')

register = False
i = 0

while not register:
    print('회원가입을 진행하시겠습니까? \n ( N : 취소 / Y : 진행 )')
    register_input = input('>> ')
    # 대문자, 소문자 모두 받아서 진행하도록 함
    register_input = register_input.lower()
    
    
    if register_input == 'y':
        register = True
        
        print('==============================\n')
        print("회원가입을 진행하겠습니다! \n")
        print('==============================\n')
        
    elif register_input == 'n':
        
        print('==============================\n')
        print("회원가입을 취소하겠습니다 \n")
        print('==============================\n')
        
        exit() # 프로그램을 종료시키는 메서드 
        
    else:
        i += 1
        print(f'{i}번 잘못 입력하셨습니다 ')
        
        if i == 3:
            print('3번 잘못 입력하셨습니다.\n\n프로그램을 종료합니다.')
            exit()

i = 0
users = []

while True:
    
    user = {}
    
    username = input('ID: ')
    while True:
        password = input('PW: ')
        password_confirm = input('PW 확인: ')
        if password_confirm == password:
            break # while 문을 빠져나오는 역할
        else:
            print('패스워드가 일치하지 않습니다.')
            
    name = input('이름: ')
    while True:
        birth_date = input('생년월일(6자리): ')
        if len(birth_date) == 6:
            break
        else:
            print('생년월일 입력값이 올바르지 않습니다. ')
            
    email = input('E-mail: ')
    
    # 입력받은 값들을 할당함
    user['username'] = username 
    user['password'] = password
    user['name'] = name
    user['birth_date'] = birth_date
    user['email'] = email
    
    users.append(user)
    print(users)
    
    print('==============================\n')
    print(f"{user['name']} 님, 가입을 환영합니다!\n")
    print('==============================\n')
    
    print('회원가입을 추가로 진행하시겠습니까? \n ( N : 취소 / Y : 진행 )')
    
    register_another_input = input('>>')
    register_another_input = register_another_input.lower()
    
    if register_another_input == 'y':
        pass # 어떠한 작업도 수행하지 않고 if문을 빠져나옴
    elif register_another_input == 'n':
        exit()
    else:
        print(f'{i}번 잘못 입력하셨습니다 ')
        
        if i == 3:
            print('3번 잘못 입력하셨습니다.\n\n프로그램을 종료합니다.')
            exit()
    
