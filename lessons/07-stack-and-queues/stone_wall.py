# Codility lesson
# https://codility.com/programmers/task/stone_wall/
# 40 minutes

fi = open('stone_wall.in')

T = int(fi.readline())

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(H):
    block_count = 1
    blocks = []
    blocks.append(H[0])

    for elem in H[1:]:
        if blocks[-1] == elem:
            continue # no need to use new block
        elif blocks[-1] < elem:
            blocks.append(elem)
            block_count += 1
            continue

        while(blocks and blocks[-1] > elem):
            # print elem
            blocks.pop()

        if blocks and blocks[-1] == elem:
            continue
        else:
            block_count += 1
            blocks.append(elem)

        # print blocks

    return block_count

for t in xrange(T):
    H = [int(x) for x in fi.readline().split(' ')]
    output_val = solution(H)
    print output_val