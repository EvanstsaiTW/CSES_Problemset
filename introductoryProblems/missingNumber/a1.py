n = int(input())

inputNum = set([int(x) for x in input().split()])
totalNum = set([int(x) for x in range(1, n+1)])
difference = totalNum.difference(inputNum)
print(difference.pop())
