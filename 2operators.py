#user input - input
i="hi89"
# a= input("Enter value ")
# a= int(input("Enter value "))
# print("value of a is",a)
# print(type(a))

# b=int(input("Enter b "))
# print(a+b)

# Arithmetic Operators - +,-,*,/,%,** 

# a=int(input("Enter a "))
# b=int(input("Enter b "))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# Assignment Operators - =,+=,*=,-=,/=
a=20
a+=10  # a=a+10 -- 30
a-=15  # a=a-15 --- 15
a*=10
a/=15

print(a)

# Relational or Comparison operator -- >,<, >=,<=,!=,==  - True or False 
print(15>13) 
print(13>=13)
print(45<19)
print(33!=33)
print(45==14) 

print("Logical operators") # True or False , --- and , or, not

print(True or True or False)
print(True and True and True and False)

print(11>45 and 55>30)
print(11>10 or 55>10 or 10>78)

#membership operators in, not in - True or False
print("Membership Operator")

naam="Gurminder singh"
print("uri" in naam)
print("uri" not in naam)


# id concept 
# i=10
# j=10
# print(id(i))
# print(id(j))
# print("-----")
# k='hi'
# l='hi'
# print(id(k))
# print(id(l))

i=int(input("enter i "))
j=int(input("enter j "))
# i=input("enter i ")
# j=input("enter j ")
print(id(i))
print(id(j))
# identity operator is, is not
m=10
o=10

# print( m is o)
print( i is j)
