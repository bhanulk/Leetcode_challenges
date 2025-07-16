import collections
oddfreq=0
str1=input("")
frq=collections.Counter(str1)
for value in frq.values():
    if value%2!=0:
        oddfreq+=1
if oddfreq>1:
    print("Not palindrome")
else:
    print("Palindrome")
    
