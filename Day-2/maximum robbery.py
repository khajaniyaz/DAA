'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are
arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security systems connected, and it
will automatically contact the police if two adjacent houses were broken into on the same night.''''

def robber(money):
    even_amt,odd_amt=0,0
    for i in range(0,len(money)-1):
        if(i%2==0):
            even_amt+=money[i]
        else:
            odd_amt+=money[i]
    return even_amt if even_amt>odd_amt else odd_amt
print(robber([2,3,2]))

Output:3
