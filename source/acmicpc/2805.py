n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))

max_height = max(trees)
height_fit = 0

def get_tree_length(height):
    global trees
    total = 0
    for t in trees:
        if t > height:
            total += t - height
    return total


def bs(start, end):
    global trees, m, height_fit
    while start <= end:
        height = (start + end) // 2
        length = get_tree_length(height)
        # print("length: " + str(length))
        # print("start: " + str(start))
        # print("end: " + str(end))
        # print("height: " + str(height))
        if length == m:
            height_fit = height
            return
        elif length < m:  # 길이 부족할때 높이를 낮춰야함.
            # print("length 넉넉함, 높이 낮춤")
            end = height - 1
        else:  # 길이가 넉넉할때
            start = height + 1
            # print("length 넉넉함, 최적 높이 갱신: " + str(max(height, height_fit)))
            height_fit = max(height, height_fit)
        # print("______________________")


bs(0, max_height)
print(height_fit)
