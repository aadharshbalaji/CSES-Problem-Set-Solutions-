import sys
#sys.stdin,sys.stdout = open("input.txt",'r'),open("output.txt",'w')


"""
For attacking knights - The 2 knights attacks
each others in min length of board at 2x3 or 3x2
And in both 2x3 or 3x2 board there are 2 possible 
combination to attack. Finding how many 2x3 or 3x2 
board fits in nxn board in (n-1)*(n-2) or (n-2)*(n-1)
for adding up it gives 2*2*(n-1)*(n-2)

"""

def solve():
    n = int(input())
    for i in range(1,n+1):
        all_combination = ((i*i) * ((i*i)-1))//2
        attacking_knights = 4*(i-1)*(i-2)
        print(all_combination-attacking_knights)


def main():
    solve()
main()