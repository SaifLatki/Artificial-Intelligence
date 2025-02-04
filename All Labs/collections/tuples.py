tup=(10,10,20,30,40,50,60)
tup2=(70,80,90)
set={70,80,80,70,90}
list=[1,2,3,4]

#tup.__add__(set) //can't add this beause we can't change the values of tuples
#tup.__add__(list)//can't add this beause we can't change the values of tuples
tup=tup.__add__(tup2)
print(tup)