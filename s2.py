flowers = int(input())
all = []
for i in range(flowers):
    hold = input().split(" ")
    all.append(hold)

def makeNum(seq):
    hold = []
    for i in seq:
        hold.append(int(i))
    return hold

for i in range(len(all)):
    all[i] = makeNum(all[i])

def rotate(seq, num):
    final = []
    for x in range(num):
        hold = []
        for i in seq:
            hold.append(i[-x-1])
        final.append(hold)
    return final

def sorting(seq):
    compare = []
    for i in seq:
        control = sorted(i)
        compare.append(control)
    compare.sort()
    return compare

for i in range(5):
    if all == sorting(all):
        break
    else:
        all = rotate(all, flowers)

for i in all:
    print(*i, sep=" ")