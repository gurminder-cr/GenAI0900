# strings - 
n="Rajiv Kumar"
print(n)
print(type(n))

# methods- 
print(n.upper())
print(n.lower())
print(n.capitalize())
print(n.title()) 
print(n.swapcase())
print(n.endswith('ar')) # True Or False 
print(n.endswith('aR')) # True Or False 
print(n.startswith('Ra')) # True Or False 
print(n.find('io')) # return -1 if substring is not found
# print(n.index('io')) # raises value error if substring is not found


# replace - 
print("----------------------")
print(n)
print(n.replace('a','iu'))


# split
print("----------------------")
j="Hello class how are you"
print(j.split('o')) # by default space ke saath split krrta hai aur space include nahi hoggi


i="sfhvsf@ndfbjehd@bdhbd@jfbvdkj"
print(i.split("@"))


# strip
print("----------------------")
u="   helllo   class    "
print(u)
print(u.strip())
print(u.lstrip())
print(u.rstrip())


print(n.count('a'))

# slicing - 
print("====================")
print(n)
print(n[:]) # start:stop:step [] subscriptable operator
print(n[:4]) # start:stop:step [] subscriptable operator
print(n[:5])
print(n[2:])
print(n[::])
print(n[::1])
print(n[::2])
print(n[::-1])
print(n[1:10:-1])
print(n[10:1:-1])



# for i in "Gurminder":
#     print(i+"-",end="")
    
    
# formatted string 
a=10
b=20
print("value of a is",a,"b is",b,"this is the value")
print(f"value of a is {a} and b is {b} and this is the value")
