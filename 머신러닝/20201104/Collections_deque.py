from collections import deque

# 걍 리스트 생성해서 어팬드 하는거

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)

deque_list.rotate(1) #roate 는 (수)만큼 >> 로 옮김
print(deque_list)
deque_list.rotate(1)
print(deque_list)

print(deque_list)
print(deque(reversed(deque_list)))

deque_list.extend([5, 6, 7])
print(deque_list)


print(deque_list.index(0)) #0번쨰 인덱스의 값 가져오기
