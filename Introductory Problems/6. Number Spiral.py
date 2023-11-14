import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')
 
def solve():
    x,y = map(int,input().split())
    high = max(x,y)
    diff = abs(x-y)
    edge = high**2 - high + 1
    ans = -1
    if (high==x and (high & 1)) or (high==y and not (high & 1)):
        ans = edge - diff
    else:
        ans = edge + diff
    print(ans)
def main():
    for _ in range(int(input())):
        solve()
main()
