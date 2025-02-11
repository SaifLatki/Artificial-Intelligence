import array as arr

num_list=[2,3,4,5,63,3,223,2,23,24,4]
num_arr=arr.array('i',num_list)

print(num_arr[2:5])
print(num_arr[:-5])
print(num_arr[5:])
print(num_arr[:])