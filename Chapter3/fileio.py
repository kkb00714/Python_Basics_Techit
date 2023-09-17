# 파일 읽기/쓰기

# 파일을 읽기 위해선 open('파일 주소?', '어떤 모드로 읽을지')

# 절대경로 : c:\Users\...\literature\lyrics.txt
# => 어느 곳에서든 참조했을 때, 동일한 곳을 가리킴

# 상대경로 : literature/lyrics.txt
# => 대부분의 코딩을 할 때에는 상대경로를 사용

# f = open('literature\lyrics.txt', 'r', encoding='UTF-8') # r은 읽기모드

# print(f.read()) # 파일을 읽기 위해서는 f.read()를 실행시켜야 함
# print(f.readline()) # f.readline() 라인 단위로 txt를 읽어들임
# print(f.readlines()) # 여러 줄을 리스트로 반환함

# f.close() # 파일 작업 후  f.close()를 통해 파일을 다시 닫아줘야 함

# ------------<만약 f.close() 로 매번 닫아주기 귀찮다면?>------------
# with문을 사용하여 구성이 가능하다!
# with open('literature\lyrics.txt', 'r', encoding='UTF-8') as f:
#     print(f.read()) 

# -------------<파일 작성 방법!>-------------

# w 모드는 기존의 내용을 전부 삭제시킴
f = open('literature\lyrics.txt', 'w', encoding='UTF-8')
f.write("새로운 글이 작성되었습니다.")

f.close()

# a 모드는 기존의 내용을 삭제하지 않고 
# 뒤에 덧붙이게 됨
f = open('literature\lyrics copy.txt', 'a', encoding='UTF-8')
f.write("\n새로운 글이 작성되었습니다.")

f.close()



