# 반복문(loops)

# i = 0
# sum = 0

# range 에서 범위 지정 가능
# for i in range(1, 101): # 1부터 101 미만 이라는 범위를 지정해줌
#     print(i)
    
# for i in range(1, 101):
#     sum = sum + i
    # 초기화된 sum 이라는 변수에 i 값을 더해서 출력

# print(sum)

# -----------< while 사용 >-------------

# while은 범위를 설정하지 않으면 계속해서 반복하므로 범위를 설정해줘야 함
# while True:
#     print("리얼리 감덩실화 참트루입니다")

progress = 0

while progress < 100:
    progress = progress + 1
    print(f"{progress}% completed")

