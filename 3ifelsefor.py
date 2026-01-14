# if ,else, elif 
# a=int(input("Enter a "))
# print(a)

# if a>10:
#     print("a is greater than 10")
# elif a==10:
#     print("a is equal to 10")
# else:
#     print("a is smaller than 10")

# marks= int(input("Enter Marks "))
# if marks>=90 and marks<100:
#     print("A Grade")
# elif marks>=80 and marks<90:
#     print("B Grade")
# elif marks>=70 and marks<80:
#     print("C Grade")
# elif marks>=60 and marks<70:
#     print("D Grade")
# elif marks<60:
#     print("Fail")
# else:
#     print("Invalid Marks")
    

# if True:
#     print("Hello")
# naam="Himanshu"
# if "an" in naam:
#     print("an is present in naam")


# values swap a,b
a=10
b=20
# third variable -- 
# temp=a
# a=b
# b=temp 


# i,j,k=11,12,13
# short method - 
a,b=b,a
print("a is",a)
print("b is",b)

# a is 20
# b is 10



# for loop -- range()

# for i in range(0,5):  # start, stop, step  -- stop-1
#     print(i)


# for i in range(0,5):  # start, stop, step  -- stop-1
#     print("Himanshu",i)

# for i in range(5):  # start by default starts from 0 
#     print("Himanshu",i)
    
    
# for j in range(1,13,2):
#     print(j)

# for j in range(10,1,-1):  #stop 1 ,  1-(-1), 2
#     print(j)
    
# for i in range(12,1,-2):
#     print(i)

# for i in range(0,50,2):
#     print(i,end=",")

for i in range(0,50):
    if i%2==0:
        print(i,end=",")