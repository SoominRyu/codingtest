#큐 구현 시 리스트 이용해도 되지만, 시간 복잡도 높음
#deque 라이브러리 이용할 것

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

#들어온 순서대로 출력
print(queue)

#역순
queue.reverse()

#나중에 들어온 원소부터 출력
print(queue)