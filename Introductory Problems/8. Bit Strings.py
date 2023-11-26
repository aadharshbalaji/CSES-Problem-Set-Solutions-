import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')

def solve():
    n = int(input())
    print((2**n)%(10**9 + 7))



def main():
    solve()
main()