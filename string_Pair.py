arr_v = [2, 2, 1, 2, 2, 2, 1, 2, 2, 2]
arr_l = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

n = int(input())

arr_n = list(map(int,input().strip().split()))[:n]

D = 0
for i in range(n):
	D = D + arr_v[int(arr_n[i])]


index = 1
pairs = []
for e1 in arr_n:
    for e2 in arr_n[index:]:
        pairs.append((e1, e2))
    index += 1
l = len(pairs)

count = 0
for i in range(l):
	s = pairs[i][0] + pairs[i][1]
	if s == D:
		count = count + 1

print(arr_l[count])