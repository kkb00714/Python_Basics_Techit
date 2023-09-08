# 조건문

# : (콜론) 으로 코드 블록을 시작한다고 알림
# if False: 
#     print("True 입니다!")
    # ☆들여쓰기가 제대로 되어있지 않으면 실행이 안 됨!☆
# else:
    # 참이 아닌 나머지 모든 경우에, else에 있는 것을 실행
    # print("False 입니다!")
    
# if 4 > 3:
#     print("a")
# else: 
#     print("b")

# value = input("값을 입력해주세요: ")

# if int(value) > 10: # 이제 입력받은 value 값을 int 값으로 받아들임
#     print("10보다 크다잉")
# else:
#     print("10보다 작다잉")

# value = value.upper() # 전처리

# if value == "ENFJ":
#     print("오! 세계 인구의 0.5% !!!!")
# else:
#     print("음^^")

# -------------< 다중 조건 >--------------

day = input("요일을 입력해주세요(0~6): ")

if day == "0":
    print("일요일 휴묿")
elif day == "1":
    print("월요일 좋아~ 최고로 좋아~")
elif day == "2":
    print("화요일 정상영업 합니다~")
elif day == "3":
    print("수요일 정상영업 합니다")
elif day == "4":
    print("목요일... 정상영업 합니다...")
elif day == "5":
    print("그...음...요일... 불금!!!!!!!!!!! 이지만 정상영업합니다....")
elif day == "6":
    print("퇼, 정상영업@!!")
else:
    print("그뭔씹")
