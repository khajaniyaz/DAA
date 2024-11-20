'''Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order. A substring
is a contiguous sequence of characters within a string'''
words=["leetcode", "et", "code"]
result=set()
for i in range(len(words)):
    for j in range(len(words)):
        if i!=j and words[i] in words[j]:
            result.add(words[i])
print(list(result))

Output:['et', 'code']
