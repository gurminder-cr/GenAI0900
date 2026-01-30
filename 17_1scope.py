# local scope 
# global scope
# functional scope 

a=10
print("before function",a)
def changeValue():
    global a
    a=20
    print("Inside function",a)

changeValue()

print("After function",a)