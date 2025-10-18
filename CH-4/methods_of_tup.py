a=(1,45,342,3424,False, "Rohan", "Shivam")
print(type(a))
#a[0]=67#Can't change
print(a)
no=a.count(False)#Howmany required elements are present in the tuple
print(no)
i=a.index(3424)#index from 0 to the allocated location of the element
print(i)

my_tuple=(1,2,3)
d, b, c=my_tuple
print(d,b,c)
