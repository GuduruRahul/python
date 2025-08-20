my_tuple = ("Sample Name", "RollNo:12345", "age:20", "gender:male")
print(my_tuple)

# tuple data access
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[-1])
print(my_tuple[0:-2])
print(my_tuple[-3])

# tuple length
print(len(my_tuple))

# tuple count
print(my_tuple.count("Sample Name"))

# tuple index
print(my_tuple.index("gender:male"))

# modifying data in tuples
# tuple to list
my_list = list(my_tuple)
print(my_list)

print(type(my_list))
my_list.append("Ph.no:9876543210")  # list append
print(my_list)

my_list.remove("age:20")  # list remove
print(my_list)

my_list.insert(4, "EEE")  # list insert
print(my_list)

# list to tuple
my_tuple_
