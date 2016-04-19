# Codility lesson
# https://codility.com/programmers/task/equi_leader/
# Correctness: 100%
# Performance: 75%

fi = open('equi_leader.in')
fo = open('equi_leader_temp.out', 'w')
T = int(fi.readline())

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, N):
    equi_leader_count = 0
    if N == 1:
        return 0

    split_index = 1
    count_first = {}
    count_second = {}

    # Initialization
    for i in range(split_index):
        if A[i] not in count_first:
            count_first[A[i]] = 1
        else:
            count_first[A[i]] += 1
    for i in range(split_index, N):
        if A[i] not in count_second:
            count_second[A[i]] = 1
        else:
            count_second[A[i]] += 1

    count = check_equi_leader(count_first, count_second, 1, N - 1)
    # print count
    if count is not None:
        equi_leader_count += 1

    for split_index in range(1, N):
        H1 = split_index
        H2 = N - split_index
        if A[split_index] in count_first:
            count_first[A[split_index]] += 1
        else:
            count_first[A[split_index]] = 1

        count_second[A[split_index]] -= 1
        count = check_equi_leader(count_first, count_second, split_index + 1, N - 1 - split_index)
        if count is not None:
            equi_leader_count += 1

        if count_second[A[split_index]] == -1:
            print "ERROR count_second"

    return equi_leader_count

def check_equi_leader(count_first, count_second, len_first, len_second):
    print '===> first'
    print count_first
    print len_first
    print '===> second'
    print count_second
    print len_second
    leader = None
    if len_first < len_second:
        leader = find_leader(count_first, len_first)
        if leader is None:
            return None

        if count_second.get(leader, 0) <= len_second/2.:
            return None
    else:
        leader = find_leader(count_second, len_second)
        if leader is None:
            return None
        if count_first.get(leader, 0) <= len_first/2.:
            return None

    print "*******leader = %s\n" % leader
    return leader


def find_leader(count, l):
    half = l/2.
    # print half
    for k, v in count.iteritems():
        # print '%s - %s' % (k, v)
        if v > half:
            # print k
            return k
    return None

for t in xrange(T):
    A = [int(x) for x in fi.readline().split(' ')]
    N = len(A)
    output_val = solution(A, N)
    print output_val
    fo.write('%s\n' % output_val)