# user defined functions, pre-defined(print, input, sum)
# def - keyword 

# def summs():
#     print("hello")
#     print("Class")
# def summs():
#     print(12+56)

# def summs():
#     a=int(input('enter a '))
#     b=int(input('enter b '))
#     print(a+b)
    
# summs()

# function with arguments 

# def addNum(a,b): #parameters 
#     print(a+b)
#     print(a*b)


# # addNum(2,4)  # arguments 

# i=int(input("Enter i "))
# j=int(input("Enter j "))
# addNum(i,j)  # arguments 


# function with return 
# ans=0
# def addNumbers(a,b):
#     # return a+b
#     print(a+b)
#     return "hi"
#     # print(ans)

# i=int(input("Enter i "))
# j=int(input("Enter j "))
# ans= addNumbers(i,j)
# print(ans)



# function with keyword arguments 

# def keyFunc(a,b,c):
#     print(a,b,c)
    
# i=10
# j=20
# # keyFunc(a=10,b=20)
# # keyFunc(j,i)
# keyFunc(c=20,a=10,b=30)




# odd number 

# def oddNumber(a):
#     if a%2!=0:
#         # return "Odd"
#         print("Odd")
#     else:
#         print("Even")
#         # return "Even"

# i=int(input("Enter Number "))
# print(oddNumber(i))



# Arbitrary Arguments - *args  - *variable_name

# def numAdd(*a):
#     # return a
#     s=sum(a)  # built-in function-sum
#     # for i in a:
#     #     s+=i
#     return s


# print(numAdd(12,15))
# print(numAdd(12,15,45))
# print(numAdd(12,15,45,56))
# print(numAdd(12,15,45,56,11))
# # numAdd(12,15)

# keyword Arbitrary Arguments **kwargs 

def addKNum(**a):
    return a

print(addKNum(a=10,b=24))
print(addKNum(a=10,b=24,c=22))
print(addKNum(a=10,b=24,c=22,d=10,e=44))