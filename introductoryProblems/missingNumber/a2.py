#hard to understand!
'''
in order to find a missing number just add a sequential sum and calclate the differce of input
'''
n = int(input())
s = 0
inputNum = [int(x) for x in input().split()]

for i in inputNum:
    s += i
print(n*(n+1)//2-s)