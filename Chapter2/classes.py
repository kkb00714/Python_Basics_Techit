# 클래스(Classes) - 설계 

# class 클래스이름(첫 문자는 대문자로)
class Student:
    
    # init 메서드 => 설계도인 class를 통해서 
    # 구체적으로 어떠한 인스턴스를 만들어주는 역할
    # self가 꼭 앞에 있어야 한다!
    def __init__(self, name, major): #, is_graduated):
        self.name = name 
        #self.name => 클래스에서 대입받는 구역
        # name => 생성자에서 인자로 넘겨받는 값
        self.major = major
        self.is_graduated = False # self.is_graduated = is_graduated
        
    def study(self):
        print(f'{self.name} 학생은 공부중입니다!')
        
    
    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'전공이 {new_major} 으로 변경되었습니다!')
    
#------------< 인스턴스 - 실체화된 사물 >-------------

student_1 = Student('김테킷', '물리학') #, False)
student_1.study()

student_1.edit_major('기계공학과')

student_1_graduated = student_1.is_graduated
print(student_1_graduated)


# print(student_1) # 주솟값이 나옴

# 각각의 Attribute 에 접근하는 방법들
# student_1_name = student_1.name
# print(student_1.name)




