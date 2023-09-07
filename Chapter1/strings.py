# -------------< 문자열(Strings) = 문자의 나열 >---------------

# city = "seoul"
# print(city)

# city.upper() 
# print(city)

# 이 코드가 제대로 안 되는 이유 : 
# upper 와 lower는 문자열을 바꾸지 않고,새로운 문자열을 반환하기 때문
# 따라서 새로운 문자열을 아래와 같이 변수에 할당해주어야 함.

# print(city.upper()) # => 문자열을 대문자로 변환해준 것을 출력

# city = city.upper() # => 문자열에 대문자로 ☆재할당☆함.
# print(city)

# city.lower()
# print(city)

# city.lower() # => 문자열을 소문자로 변환해준 것을 출력
# print(city.lower)

# city = city.lower() # => 문자열에 소문자로 ☆재할당☆함.
# print(city)

# -------------< rstip(오른쪽 공백 제거) / lstrip(왼쪽 공백 제거) / strip(양쪽 공백 제거) 사용 >---------------

# occupation = "     developer  "
# print(occupation)

# occupation.rstrip()
# print(occupation.rstrip())

# occupation.lstrip()
# occupation.strip()
# => 이 두 코드들도 나중에 변수에 재할당 해줘야 함.
# 왜냐? occupation 변수 자체는 변하지 않기 때문.

# -------------< /(백슬래시) 활용 >---------------

# print("ENFJ\nESFP\nINTJ\nISFP") # 엔터를 한 것과 동일함 (\n)
# print("ENFJ\tESFP\tINTJ\tISFP") # 탭의 간격만큼 공백을 넣음 (\t)

# -------------< 문자열 제거 >---------------

# score = "점수 : 90"
# print(score.removeprefix("점수:")) # 문자열의 시작 부분에 "점수:" 가 있으면 제거

# score_2 = "75점"
# print(score_2.removesuffix("점")) # 가장 끝 부분에 있는 "점" 이라는 문자만 제거

# -------------< 문자열 교체 >---------------

# city = "서울 노원구"
# print(city.replace("서울", "서울시")) # .replace("바꿀 문자열", "바꾸고 싶은 문자열")

# -------------< fstring 활용 >---------------

si_1 = "양주"
gu_1 = "용인"

si_2 = "덕정"
gu_2 = "처인"

si_3 = "10"
gu_3 = "밥먹"

print(f"{si_1}시 {gu_1}구") # 따옴표 바깥쪽에 f 사용 후 중괄호에 변수명 입력하기
print(f"{si_2}시 {gu_2}구")

address_1 = f"{si_3}시에 {gu_3}구" # f string 자체를 변수에 할당하는 방법
print(address_1)