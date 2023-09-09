# 리스트(lists)

# mbti = ['ENFJ', 'INFJ', 'CUTE', 'ESTP']

# print(mbti)
# print(mbti[0])

# mbti[0] = 'ENFP' 
# 리스트를 따로 선택해서 지정해줄 수 있다!

# print(mbti)
# print(mbti[0])


# my_list = [123, 'apple']
# print(my_list)

# colors = ['red', 'blue', 'green']

# 수정 (green -> black)
# colors[2] = 'black'
# print(colors)

# 추가1 (append) => 리스트의 가장 마지막에 새로운 요소를 추가함
# colors.append('purple') 
# print(colors)

# 추가2 (insert) => 원하는 인덱스에 값 넣기가 가능함
# colors.insert(1, 'green')
# print(colors)

#--------------< 리스트에 추가하는 방법은 append, insert 두 가지가 있다! >---------------

# 제거1 (del) => (이 값을 지울 수는 있어도 활용할 수 있는 방법은 없음.)
# del colors[0]
# print(colors)

# 제거2 (pop) => (제거와 동시에, 이 데이터를 사용할 수 있도록 컴퓨터가 반환해줌.)
# color = colors.pop(0)
# print(colors)
# print(color)

# 제거3 (remove) => (리스트에 속해있는 값을 직접 입력해서 삭제함.)
# colors.remove('blue')
# print(colors)

#--------------< 리스트에서 제거하는 방법은 del, pop,  가지가 있다! >---------------

# 리스트 정렬

colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 정렬 1 (sort) => 리스트에서 오름차순으로 정렬해줌.
# colors.sort()
# print(colors)

# 정렬 2 (sort(reverse=True)) => 리스트에서 내림차순으로 정렬해줌.
# colors.sort(reverse=True)
# print(colors)

# 정렬 3 (sorted()) => 기존에 있는 배열을 '잠깐' 순서대로 정렬했다가,
# 저 코드를 벗어나면 다시 원래대로 돌아감
# sorted(colors)
# print(colors) # == print(sorted(colord))

# 길이 - 요소의 갯수
# print(len(colors))

# 가장 마지막에 있는 요소를 가져옴
# print(colors[-1])


