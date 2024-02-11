T = int(input())
from collections import deque


def bfs(graph, M, N, startx, starty, visited):
    q = deque([[startx, starty]])
    if visited[startx][starty]:
        return 0
    visited[startx][starty] = True
    while q:
        # 세로가 x, 가로가 y
        x, y = q.popleft()
        ds = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for d in ds:
            nextX, nextY = x+d[0], y+d[1]
            if nextX > N-1 or nextY > M-1 or nextX < 0 or nextY < 0:
                continue
            if graph[nextX][nextY] == 1 and not visited[nextX][nextY]:
                visited[nextX][nextY] = True
                q.append([nextX, nextY])
    return 1



for i in range(T):
    M, N, K = list(map(int, input().split()))  # 가로 M, 세로 N, 배추 개수 K.
    # 격자에 접근할 때는 graph[세로인덱스][가로인덱스]이고, 최대 인덱스는 M-1, N-1임에 주의.
    graph = []
    visited = []
    for x in range(N):
        graph.append([0 * _ for _ in range(M)])  # 그래프 초기화
        visited.append([False * _ for _ in range(M)])

    xys = []
    for k in range(K):
        y, x = list(map(int, input().split())) # 가로, 세로 형식으로 들어오는데 세로가 2차원 배열의 첫번째 인덱스로 들어가야함
        graph[x][y] = 1
        # xys 배열에는 세로, 가로순으로 들어감.
        xys.append([x, y])
    mintotal = 0
    for xy in xys:
        x, y = xy
        mintotal += bfs(graph, M, N, x, y, visited)
    print(mintotal)