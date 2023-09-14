# 회원가입을 구현해보자! 

print('==============================\n')
print('회원가입\n')
print('==============================\n')

register = False
i = 1

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
        print('잘못 입력하셨습니다 ')
        # while i < 4:
        #     print(f"{i}번 잘못 입력하셨습니다.")
        #     i += 1
            
        #     if i == 3:
        #         print('세 번 이상 잘못 입력하셨습니다. \n')
        #         print('프로그램을 종료합니다.')
        #     exit
            
        

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
    
    
    
    
