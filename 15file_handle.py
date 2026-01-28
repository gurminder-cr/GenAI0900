# files - read, write, append 

# 1st method - file 
# f= open('file.txt','r')  # r- read
# print(f.read())
# f.close()


# f= open('file.txt','w')  # w- write
# i="Arshdeep Jatin "
# f.write(i)
# f.close()

# f= open('file.txt','a')  # a- append
# i=" Anshu Mehak Mansi"
# f.write(i)
# f.close()

# 2nd method -

# with open('file.txt','r') as f:
#     print(f.read())


# with open('file.txt','r+') as f:
#     print(f.read())
#     f.seek(2)
#     f.write("Hello")


with open('file.txt','w+') as f:
    f.write("Jatin Dhuper")
    f.seek(0)
    print(f.read())


# with open("new.txt",'x') as e:
#     print(e.write("hello"))


# Json files read