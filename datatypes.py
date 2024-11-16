#numeric type


#integers

a=1
print(type(a))


#float

b=1.5
print(type(b))

#complex number

c=2+3j
print(type(c))


#sequence type

#string

a="Rucha"
print(type(a))

#accessing

b="Geeks for geeks"
print("First character of string")
print(b[0])
print("Last character of string")
print(b[-1])


#list
a=["Rucha","Chavan"]
print(type(a))


#accessing
list=["Geeks","For","Geeks"]
print("Accesing element from list:")
print(list[0])
print(list[2])
print("Accesing element with negative index:")
print(list[-1])
print(list[-2])

list=[1,3,2,0,4]
list1=[5,6,7,8,9]
print ("Printing the original list")
for i in list:
    print(i,end='')
list.reverse()
print ("\nPrinting list after the reversing")
for i in list:
    print(i,end='')


#tuple
a=1,2,3
print(type(a))


#accessing
tuple="Rucha","Chavan"
print(tuple[0])
print(tuple[-1])

#conversion of tuple to list
rucha_t1=(1,2,3)
rucha_list =[*rucha_t1]
print(rucha_list)


#adding
t1=(1,2,3)
t2=(2,3,4)
t1=t1+t2
print(t1)

#count
t1=(0,1,2,3,4,7,6,4,3)
res=t1.count(4)
print("Count of 4 in t1 is:",res)

#boolean
a=True
print(type(a))


#set
s1=set()
print(s1)
s1.add("DYP")
print(s1)

#adding
s1=({"Autumn","Spring","Winter"})
print("The original set",s1)
print("The set after adding")
s1.add("Summer")
print("The set after adding",s1)

#remove
s1=({"Autumn","Spring","Winter"})
print("The original set",s1)
print("The set after Removing")
s1.remove("Spring")
print("The set after removing",s1)

#union
Day1={'Jan','Feb','March','April','May','June'}
Day2={'July','August','Sep'}
print(Day1.union(Day2))

#dictionary
Emp={"Name":"Siddhant","age":20,"salary":250000}
print(type(Emp))
print(Emp)

#accessing
emp1={"Name":"Siddhant","age":20,"salary":250000}
print(emp1['Name'])




