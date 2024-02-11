N, r, c = list(map(int, input().split()))
i = 0
total = 0


def is_in(startx, starty, endx, endy):
    global r, c
    return startx <= c <= endx and starty <= r <= endy


def split(startx, starty, endx, endy, size):
    global N, r, c, i, total

    if not is_in(startx, starty, endx, endy):
        i += size ** 2
        return

    if size == 1:  # 크기가 1일때
        if startx == c and starty == r:
            total = i
            print(total)
            exit(0)
        i += 1
        return

    xmid = (endx + startx) // 2
    ymid = (endy + starty) // 2
    size //= 2

    split(startx, starty, xmid, ymid, size)
    split(xmid + 1, starty, endx, ymid, size)
    split(startx, ymid + 1, xmid, endy, size)
    split(xmid + 1, ymid + 1, endx, endy, size)


split(0, 0, 2 ** N - 1, 2 ** N - 1, 2 ** N)
