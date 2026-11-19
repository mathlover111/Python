data = [16, 25, 39, 27, 12, 8, 45, 43]
for i in range(len(data)):
    print('%3d' % data[i], end='')
print()

for i in range(len(data) - 1, 0, -1):
    for j in range(i):
        if data[j] > data[j + 1]:
            data[j + 1], data[j] = data[j], data[j + 1]
    
    # 印出每一輪排序後的結果（對齊第 7 行的縮排層級）
    print('第 %d 次掃描後的結果是：' % (len(data) - i), end='')
    for j in range(len(data)):
        print('%3d' % data[j], end='')
    print()

print('排序後結果為：', end='')
for i in range(len(data)):
    print('%3d' % data[i], end='')
print()