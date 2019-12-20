data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 10 == 0:
            print(len(data))
print('讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))


new = []
for d in data:
    if len(d) < 59:
        new.append(d)
print('一共有', len(new), '比留言長度小於59')

sceon = []
for d in data:
    if 'son' in d:
        sceon.append(d)
print('一共有', len(sceon), '筆')