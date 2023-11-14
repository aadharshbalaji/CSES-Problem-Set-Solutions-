import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')
 
def total(x):
    return int(x*(x+1)/2)
def solve():
    n = int(input())
    ip = sum(list(map(int,input().split())))
    ans = total(n)-ip
    print(ans)
def main():
    solve()
main()
