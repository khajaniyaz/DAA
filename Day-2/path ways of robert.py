'''A robot is located at the top-left corner of a m×n grid .The robot can only move either down or right at any point in time. The robot is trying to
reach the bottom-right corner of the grid. How many possible unique paths are there?'''

def robo(m,n):
    ans=(fact(m+n-2))//(fact(m-1)*fact(n-1))
    return ans
def fact(x):
    if x==0:
        return 1
    return fact(x-1)*x
print(robo(7,3))

Output:28
