T = int(input())


def printArray(arr):
    print(str(arr[0]) + " " + str(arr[1]))


for i in range(T):
    N = int(input())
    dp = [[] * _ for _ in range(N + 1)]
    if N == 0:
        printArray([1, 0])
        continue
    elif N == 1:
        printArray([0, 1])
        continue
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for j in range(2, N + 1):
        dp[j] = [dp[j - 1][0] + dp[j - 2][0], dp[j - 1][1] + dp[j - 2][1]]
    printArray(dp[N])
