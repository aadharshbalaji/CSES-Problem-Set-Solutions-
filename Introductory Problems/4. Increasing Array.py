import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')
 
def check(x,ip):
    return ip[x]<ip[x+1]
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    moves = 0
 
    for i in range(n-1):
        if not check(i,arr):
            moves += arr[i]-arr[i+1]
            arr[i+1]=arr[i]
    print(moves)
 
def main():
    solve()
main()
