# Write a Python function average_marks that accepts any number of integer marks using
# *args.
# The function should:
# 1. Ignore any mark that is less than 0 
# 2. Return the average of the remaining marks
# 3. If no valid marks are provided, return 0


# def average_marks(*a):
#     print(a)
#     n=[]
#     for i in a:
#         if i!=0:
#             n.append(i)
#     print(len(n))
#     sum=0
#     if len(n)!=0:
#         for i in n:
#             sum+=i
        
#         print(sum/len(n))
#     if len(n)==0:
#         return 0
    
# print(average_marks(12,10,0,45,56,0))
# print(average_marks(0,0,0,0,0))

# 2nd approach 
def average_marks(*a):
    valid_marks = [i for i in a if i>0]
    
    if not valid_marks :
        return 0

    print(sum(valid_marks)/len(valid_marks))
print(average_marks(12,10,0,45,56,0))


# Question 2 – **kwargs (Mediocre Level)
# Write a Python function filter_details that accepts any number of keyword arguments
# using **kwargs.
# The function should:
# 1. Print only those key–value pairs where the value is a string
# 2. Print them in the format: key = value


def filter_details(**k):
    # print(k)
    for i,j in k.items():
        # print(i,j)
        if type(j) is str:
            print(i,"=",j)
    
filter_details(a='hello',c=10,rollno=13,name='simran')