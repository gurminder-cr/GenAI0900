# string - '', ""
#     0----------11
naam="Sourav kumar"
print(len(naam))
print(naam[3])
# index slicing 

print(naam[:]) # start, stop, step 
print(naam[0:4]) # start, stop, step 
print(naam[:5]) # by default start-0
print(naam[1:5]) # by default start-0
print(naam[1:]) 
print(naam[2:15]) # 
print(naam[1:6:2])  
print(naam[1:10:-1])
print(naam[11:1:-1])    
#

# methods 
print("-----------------")
print(naam)
print(naam.upper())
print(naam.lower())
print(naam.capitalize())
print(naam.title())
print(naam.swapcase())
print(naam.endswith('ar'))  # end - substring- True or False - Case sensitive 
print(naam.startswith('so'))

print("------------")
str1= '       hello    hi      '
print(str1.strip())  # remove extra space from both side 
print(str1.lstrip())  # left space removed 
print(str1.rstrip())  # right extra space removed 

print("-------------------")
n="Himanshu Dhiman"
print(n)
# replace 
print(n.replace('an','u'))

print("-----------split----------")
i="Hello, how are you class"
print(i.split()) # by default space 
print(i.split('o')) 

j="bfhdsg#brjhfb#dbdh#dhgkfjvhdkl#ndfkjvhd#ndkjfhdfkjnd"
print(j.split('#'))

# name= input("Enter Your name ")
# print(len(name))
# for i in range(0,len(name)):
#     print(name)


name= input("Enter Your name ") 
for i in name: print(name,i)

