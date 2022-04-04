a = [-3, 5, 0, -8, 1, 10]

N = len(a)


for i in range(1, N):
    for x in range(i, 0, -1):
        if a[x] < a[x - 1]:
            a[x - 1], a[x] = a[x], a[x - 1]
        else:
            break

print(a)

