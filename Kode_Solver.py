def fil(n, n1, y, g):

    y1 = 0
    g1 = 0
    for i in range(len(str(n1))):
        if n1[i] == str(n)[i]:
            g1 += 1
        elif n1[i] in str(n):
            y1 += 1
    
    if g1 == g and y1 == y:
        return True
    else:
        return False

def solve(l, n, y, g):
    l_ = []

    for i in l:
        if fil(n, i, y, g):
            l_.append(i)
    
    return l_

n = int(input())

l = list(map(str, range(10000, 20000)))
l = [i[1:] for i in l]
for i in range(n):
    input_ = input().split()
    n1 = input_[0]
    y = int(input_[1])
    g = int(input_[2])
    l = solve(l, n1, y, g)
    print(len(l))
print(len(l), *l)