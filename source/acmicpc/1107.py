N = int(input())  # 채널
M = int(input())  # 고장버튼 개수
brokens = list(map(int, input().split()))
buttons = [i for i in range(10)]
for br in brokens:
    buttons.remove(br)

only_plusminus = abs(N - 100) # 100번에서 +, -만을 이용하여 이동
channel_len = len(str(N))

def make_number():
    global N, buttons, channel_len
    target = N
    number = -1
    for i in range(0, channel_len):
        depth = channel_len - i - 1
        top = target // (10**depth)


