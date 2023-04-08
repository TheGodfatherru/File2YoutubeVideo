from math import ceil

file = open('../What-is-Alcohol-by-Volume-or-ABV.jpg', 'rb').read().hex()

array = []
ans = []
for i in range(ceil(len(file) / 4)):
    array.append(file[i * 4: i * 4 + 4])
for i in array:
    ans.append(f"{int(i, 16):0>16b}")
print(''.join(ans))
