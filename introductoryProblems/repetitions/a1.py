array = [x for x in input()]

ans = 1
s = 1
prev = "no"
for i in array:
    if prev == i:
        s += 1   
        ans = max(ans, s)
    else:
        s = 1
        prev = i

print(ans)