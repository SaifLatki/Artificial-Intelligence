from array import *

my_array=array('i',[1,2,3,4])

for i in range(len(my_array)):
    print(my_array[i])


my_array.append(5)
print(my_array)

my_array.insert(0,0)
print(my_array)

my_array.remove(0)
print(my_array)

my_array.pop()
print(my_array)

print(my_array.index(1))
my_array.reverse()

print(my_array.count(2))

print(my_array.buffer_info())

