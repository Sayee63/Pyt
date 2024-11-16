status=input ("Enter the marital status(U/M)")
gender=input ("Enter the gender (m/f)")
age=int(input ("Enter the age"))
if status=='M':
    print ("The driver is insured")
elif status=='U' and gender=='m' and age>=30:
    print ("The driver is insured")
elif status=='U' and gender==' f' and age>=25:
    print("The driver is insured")
else:
    print ("The driver is not insured")
