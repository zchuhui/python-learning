myList = ['Monday','Tuesday',1,2]
myList.remove('Monday')
print(myList) # ['Tuesday', 1, 2]

myList = ['Monday','Tuesday',1,2]
myList.pop(0)
print(myList)  # ['Tuesday', 1, 2]

myList = ['Monday','Tuesday',1,2]
del myList[0]
print(myList)  # ['Tuesday', 1, 2]

# del myList     # 删除后，这 个list 没了
# print(myList)  # NameError: name 'myList' is not defined


myList = ['Monday','Tuesday',1,2]
myList.clear()
print(myList)    # []



