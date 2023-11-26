import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')

def divide(n):
    a = []
    start,end = 1,n
    while(start<end):
        a.append(start)
        a.append(end)
        start+=1
        end-=1
    return a

def solve():
    n = int(input())
    if n%4!=0 and n%4!=3:
        print("NO")
        return
    print("YES")
    if n%4==0:
        a = divide(n)
        a,b = a[:len(a)//2],a[len(a)//2:]
    elif n%4==3:
        a = divide(n-1)
        a,b = a[:len(a)//2+1],a[len(a)//2+1:]
        b.append(n)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)


def main():
    solve()
main()