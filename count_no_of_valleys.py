#We checking if the given string has valleys
#Logic is to count the valley if current step is 'U' and the level is 0
def countnumberofvalleys(steps):
    level=0
    count=0
    if not steps or len(steps)==1:
        return 0
    for i in steps:
        if i=='U':
            level+=1
        else:
            level-=1
        if i =='U' and level==0:
            count+=1
    return count
steps=input("Enter the string:")
print(countnumberofvalleys(steps))
    