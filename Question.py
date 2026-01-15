#
# name= input("Enter Your name ")
# print(len(name))
# for i in range(0,len(name)):
#     print(name)
    
# Write a program to find the sum of first n natural numbers(n is integer input from user)
# Print the multiplication table of a given number using a for loop
# output - 2*2=4 


# write a program to check whether a given number is prime or not.
n= int(input("Enter number "))
print(n**0.5)
if n<=1:
    print("False")
else:
    prime= True 
    for i in range(2,n):
        if n%i==0:
            prime=False 
print(prime)

# Check whether a number is a palindrome. 
# 1221 

#Print numbers from 1 to 100:
    # If divisible by 3 → print Fizz
    # If divisible by 5 → print Buzz
    # If divisible by both → print FizzBuzz

# Git Commands - 
# git --version
# git config --global user.name "Your Name"
# git config --global user.email "your.email@example.com"


# command line -- open folder 
# git init
# git clone repo_link
# git status -- to check status of your working directory 
# git add file_name  --- for specific file 
# git add --all  -- for all file 
# git commit -m "Your message"
# git push


# or 
# git pull