# dictionary - {}
# sets- {} 

# a={}
# print(a)

# s=set()
# print(type(a))
# print(type(s))


a={'name':'Arshdeep','rollno':123,'class':'btech','isownapet':True}
# print(a)

a2={
    'name':{
            'firstname':'Arshdeep',
            'lastname':'singh'
    },
    'class':'btech',
    'rollno':12,
    'address':{
        'primary':'Jalandhar',
        'temporary':'Mohali Sector 71'
    }
}

# print(a2)

print(a)
print(a['class'])
print(a['class'],a['rollno'])

# update - 2 methods

a.update(gender='Male')
print(a)

a['name']='Jatin'
print(a)
a['new']='Cricket'
print(a)


# print(a['names'])
# print(a.get('name'))
# print(a.get('names','Not present'))


# print(a.keys())
# print(a.values())
# print(a.items())


print("---------------------------")

for i in a.items():
    print(i)
print("---------------------------")
for i in a.keys():
    print(i)
print("---------------------------")
for i in a.values():
    print(i)
print("---------------------------")


print(a2)
print(a2['name']['lastname'])