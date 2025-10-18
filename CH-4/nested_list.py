nested_list = [[1, 2, 3], ["Hello", "World"]]#nested_list=[[0], [1]]
print(nested_list)
print(nested_list[1][0])#element 0 of list 1
nested_list[0].append("fruit")
print(nested_list)
nested_list[0].insert(1, "JJ")
print(nested_list)
nested_list[0].remove("JJ")
print(nested_list)
