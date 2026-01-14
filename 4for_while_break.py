# nested for loop 

# *
# * *
# * * *
# * * * *
# * * * * *


# for i in range(1,6):  # total number of lines 
#     for j in range(0,i):
#         print("*",end=" ")
    
#     print()
    
# i=1 
# while i<15:
#     print(i)
#     i+=1 # i=i+1
    
# print("value of i is",i)

# break and continue statement 

# for i in range(0,10):
#     if i==5:
#         break 
    
#     print(i)
    
for i in range(0,10):
    if i==5:
        continue 
    print(i)
    
    
    

# 7.  Ask User to input a Number and with + or - and perform followings Output
#    Enter a no: 567
#    Enter OP(+,-): +
#    0,1,2,3.......566
#    if -
#    567...>..... 1

op= input("Enter operator + or - ")
number= int(input("Enter Number "))

if op=="+":
    for i in range(0,number):
        print(i,end=",")
elif op=="-":
    for i in range(number,0,-1):
        print(i,end=",")