# 딕셔너리(Dictionaries)

# dcsnry = {"student_no":"20230911",
#            "major" : "IDN",
#            "grade" : "A+",
#            "age" : 24}

# print(dcsnry["student_no"])

# dcsnry["student_no"] = "010101010"

# print(dcsnry)
# print(dcsnry["student_no"])


# 딕셔너리에서의 값 추가
# dcsnry["gta"] = 5
# print(dcsnry)

# 딕셔너리에서의 수정
# dcsnry["gta"] = "Liberty"
# print(dcsnry)

# 딕셔너리에서의 삭제
# del dcsnry["gta"]
# print(dcsnry)


# ---------< 딕셔너리의 유용한 함수 >----------

# 데이터 접근 => (딕셔너리.get("키"))
# print(dcsnry.get("major"))
# print(dcsnry.get("gta", "해당 키-값 쌍이 없습니다."))

# 딕셔너리의 키를 전부 반환 => (딕셔너리.keys())
# print(dcsnry.keys())
# print(list(dcsnry.keys())) # 이건 리스트로 키 값을 반환하는 방법

# 딕셔너리의 값을 반환 => (딕셔너리.values())
# print(dcsnry.values())
# print(list(dcsnry.values()))

# ----------< 딕셔너리의 반복문 >------------

# tech = {
#     "Python":"Basics",
#     "SpringBoot" : "VeryDifficult",
#     "Html" : "Advanced",
#     "Me" : "Awesome"}

# for key, value in tech.items(): 
    # (tech.items()) => tech의 items에 대한 key, value 쌍을 가져옴
    # 만약 i 하나만 지정해서 print(i) 를 한다면
    # 앞의 key 값만 출력이 됨
    # print(f'{key} - {value}')
    

# for key in tech.keys(): 
    # key만 출력
    # print(key)

# for value in tech.values():
    # value만 출력
    # print(value)


# ----------< 딕셔너리의 중첩(1) >------------

# student_1 = {
#     "student_no" : "1",
#     "gpa" : "4.3"
#     }

# student_2 = {
#     "student_no" : "2",
#     "gpa" : "3.21"
#     }


# 딕셔너리들을 리스트로 만들고 싶을때 사용

# students = [student_1, student_2]

# for student in students:
    # students 리스트에 있는 딕셔너리에서 특정 값만 가져오고 싶을때 사용
    # print(student['student_no'])
    # print(student)
    
# for student in students:
    # 각 딕셔너리에 새로운 값을 추가할 때 사용
    # student['graduate'] = False
    # print(student)


# ----------< 딕셔너리의 중첩(2) >------------

# student = {
    # 딕셔너리에서의 value 값을 리스트 사용할 때
    # "subjects" : ["스프링부트", "파이썬", "C", "HTML"]
# }

# 딕셔너리의 key인 subjects의 value 값을 출력
# print(student["subjects"]) 

# subjects 의 value 값을 새로운 변수에 리스트로 할당
# subjects_list = student["subjects"]

# for subject in subjects_list:
#     print(subject)


# ----------< 딕셔너리의 중첩(3) >------------

# 딕셔너리 안의 딕셔너리
student = {
    "scholarship" : {
        "name" : "국가 장학금",
        "amount" : 1000000
    }
}

print(student)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

# 딕셔너리의 value값(또 다른 딕셔너리) 에서, 
# 그 value 값만 출력하는 코드 (value의 value값..)
for value_2 in student.values():
    for value_3 in value_2.values():
        print(value_3)

