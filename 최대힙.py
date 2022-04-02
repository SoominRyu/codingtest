#최대 힙

import heapq

#오름차순 힙 정렬
def heap(iterable):
  h = []
  result = []

  #차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
    #넣을 때 heappush
  #힙에 삽입된 모든 원소 차례대로 꺼내어 담음
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
    # 꺼낼 때 heappop
  return result

result = heap([1,3,5,7,9,2,4,6,8,0])

print(result)