
print('1.''mod1','2.''mod2','3.''append','4.''reverse')
choice=input("Enter your choice")
if(choice=='1'):
    from pack import mod1
    mod1.sum(20,5)
    print("Addition is:",sum)
elif(choice=='2'):
    from pack import mod2
    mod2.sub(10,5)
    print("Subtraction is:",mod2)
elif(choice=='3'):
    from pack import append1
    append1.append()
    print("Appended list is:",append1)
elif(choice=='4'):
    from pack import rev
    rev.reverse()
    print("Reverse string is:",rev)
else:
    print("INVALID CHOICE")



