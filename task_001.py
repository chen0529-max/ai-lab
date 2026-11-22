apple=list(map(int,input().split()))
h = int(input())
max_h = h + 30
count = 0
for height in apple:
    if max_h >= height:
        count += 1
print(count)
