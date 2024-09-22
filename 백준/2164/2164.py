"""
문제: 카드2
문제요약: 정수 n을 받은 후 마지막으로 남는 카드 번호를 반환하기
구현로직
1. n을 입력받음
2. 정수 1부터 n까지를 아이템으로 갖는 컨테이너 생성
3. 컨테이너에서 가장 앞 아이템 제거
4. 컨테이너에서 가장 앞 아이템을 맨 뒤로 보내기
5. 컨테이너에 남은 아이템의 갯수가 1개일 때까지 3,4 단계 반복
6. 남은 아이템 반환
"""

# 방법1 : deque를 활용하여 큐 구현
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

queue = deque([x for x in range(1, n + 1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)
