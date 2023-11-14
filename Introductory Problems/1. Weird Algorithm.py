import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')
 
def check_odd(x):
    return x & 1
def solve():
    n = int(input())
    ans = ""
    while(n!=1):
        ans += str(n)
        n = (3*n + 1) if check_odd(n) else int(n/2)
        ans += " "
    ans += "1"
    print(ans)
def main():
    solve()
main()
