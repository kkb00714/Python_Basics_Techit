# 딕셔너리(Dictionaries)

dcsnry = {"student_no":"20230911",
           "major" : "IDN",
           "grade" : "A+",
           "age" : 24}

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
print(dcsnry.get("major"))
print(dcsnry.get("gta", "해당 키-값 쌍이 없습니다."))

# 딕셔너리의 키를 전부 반환 => (딕셔너리.keys())
print(dcsnry.keys())
print(list(dcsnry.keys())) # 이건 리스트로 키 값을 반환하는 방법

# 딕셔너리의 값을 반환 => (딕셔너리.values())
print(dcsnry.values())
print(list(dcsnry.values()))

