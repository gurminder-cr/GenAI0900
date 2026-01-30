# Exception handling - 
# Syntax error 
# Logical error 


a=int(input("Enter a "))
b=int(input("Enter b "))

# print(a/b) 

# try: 
#     print(a/b)
# except Exception as e:
#     print("Error is",e)
# finally:
#     print("Always Executed")
l=[12,45,22]
try: 
    print(a/b)
    print(l[5])

except ZeroDivisionError as e:
    print("Error is",e)

except IndexError as e:
    print("Error is",e)
    
# except Exception as e:
#     print("Error is",e)
finally:
    print("Always Executed")
print("Hello ")

