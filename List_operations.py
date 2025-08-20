my_list = ["Sample Name", "RollNo:12345", "age:20", "gender:male"]
print(my_list)

# list append--1
my_list.append("Ph.no:9876543210")
print(my_list)

# list remove--2
my_list.remove("age:20")
print(my_list)

# list insert--3
my_list.insert(4, "EEE")
print(my_list)

# list extend--4
my_list1 = ["mail:sample123@university.edu"]
my_list.extend(my_list1)
print(my_list)

# list count--5
my_list.count("Sample Name")

# list pop--6
my_list.pop(5)
print(my_list)

# list delete--7
del my_list[4]
print(my_list)

# list reverse--8
my_list.reverse()
print(my_list)

# list sort--9
my_list.sort()
print(my_list)

# list sort reverse--10
my_list.sort(reverse=True)
print(my_list)

# list copy--11
my_list2 = my_list.copy()
print(my_list2)

# list index--12
print(my_list.index("gender:male"))

# list length--13
print(len(my_list))

# list max--14
print(max(my_list))

# list min--15
print(min(my_list))

# list clear--16
my_list.clear()
print(my_list)
