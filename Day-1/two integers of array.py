
def checker(num1, num2):
    ans=[0,0]
    for i in num1:
        if i in num2:
            ans[0]+=1
    for i in num2:
        if i in num1:
            ans[1]+=1
    return ans
num1=[1,2,2,3,4]
num2=[2,3,4,5,6]
print(checker(num1,num2))

