from collections import Counter
str1=input("enter string1:")
str2=input("enter string2:")
counter1=Counter(str1)
counter2=Counter(str2)
if counter1==counter2:
    print("Anagram")
else:
    print("Not Anagram")