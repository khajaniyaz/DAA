def firstpal(word):
    for i in word:
        if(pal(i)):
            return i
def pal(s):
    return s==s[::-1]
word=["abc", "car", "ada", "racecar", "cool"]
print(firstpal(word))

Output: "ada"
