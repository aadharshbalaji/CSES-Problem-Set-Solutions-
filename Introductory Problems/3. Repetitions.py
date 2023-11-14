import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')
 
def check(x,y,ip):
    return ip[x]==ip[y]
def solve():
    ip = input()
    start,end = 0,0
    count,max_count = 1,1
    while(end<len(ip)-1):
        end+=1
        if check(start,end,ip):
            count+=1
        else:
            count = 1
            start = end
        max_count = max(count,max_count)
    print(max_count)
def main():
    solve()
main()