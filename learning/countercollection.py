from collections import Counter

mylist = [0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,"a","a","a","a","a","a","a","a","a"]

sentences = "how many times does each word appears on the sentence of the word"


print(Counter(sentences.split()))
