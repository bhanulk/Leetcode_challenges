mapping={']':'[',')':'(','}':'{'}
string=input()
stack=[]
for c in string:
    if c=="[" or c=="(" or c=="{":
        stack.append(c)
    else:
        if stack and stack[-1]==mapping[c]:
            stack.pop()
        
if len(stack)==0:
    print("valid string")
else:
    print("invalid string")
