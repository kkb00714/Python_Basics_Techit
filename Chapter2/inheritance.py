# 상속 (Inheritance)

class Student:
    
    def __init__(self, name, major):
        self.name = name 
        self.major = major
        self.is_graduated = False
        
    def study(self):
        print(f'{self.name} 학생은 공부중입니다!')
        
    
    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'전공이 {new_major} 으로 변경되었습니다!')
        

student_1 = Student('김테킷', '물리학')
student_1.study()

student_1.edit_major('기계공학과')


# 상속을 받으려면 클래스이름() 
# => 괄호 안에 상속을 받을 부모클래스의 이름을 적어야 함
class ForeignStudent(Student):
    # 부모 클래스의 요소를 자식 클래스에서 활용할 수 있도록 하는
    # => self 를 다시 정의하지 않아도 자식 클래스에서 사용 가능
    def __init__(self, name, major, country):
        super().__init__(name, major)
        
        # ForeigStudent만 가지는 특정한 요소 추가
        self.country = country

    # 부모 클래스의 특정 메서드에 대해서 
    # 자식클래스가 원하는 방향으로 수정해서 사용
    # => 오버라이딩 (Overriding)

    def study(self): 
        print(f'{self.name} is studying now')

foreign_stud_1 = ForeignStudent('이테킷', '사회문학과', '프랑스')
print(foreign_stud_1.name)
print(foreign_stud_1.major)
foreign_stud_1.study()

foreign_stud_1.edit_major('유아교육과')
print(foreign_stud_1.edit_major)
print(foreign_stud_1.is_graduated)







