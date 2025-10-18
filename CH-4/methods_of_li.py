friends = ["apple", "orange", 5, 345, False, "Akash", "Rohan"]#Item assignment allowed

print(friends)
friends.append("Jiban")#Add in the last of the list
print(friends)

l1=[1,32,56,7,2]
l1.sort()#sort the list
print(l1)
l1.reverse()#reverse the list
print(l1)
l1.insert(3, 34)#insert 34 such that it's index in the list is 3
print(l1)
val=l1.pop(3)#pop the element in index 3
print(val)
# L=l1.remove(4) error
print(l1)
print(l1[0:4])#Slicing 
# l1+l2 = combine
# l1.extends(l2)
# repeate = l1*2  it will show repeatedly
print("apple" in friends)