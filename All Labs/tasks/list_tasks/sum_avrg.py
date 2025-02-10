sum_avrg=[1,2,3,4,5,6,7,8,9,10]
sum=0
avg=0
for i in range(len(sum_avrg)):
    sum+=i
    avg=sum/(len(sum_avrg))

print(f'sum is {sum} and average is {avg}')
