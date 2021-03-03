# # floating formatting follows " {value:width.precision f}"
# result = 100/777
# print(result)
# print("The result was {r:1.3f}".format(r=result))

# # f string
# name = "John"
# print(f'Hello, his name is {name}')
# # List suport indexing and slicing
# my_list = [1, 2, 3, 4]
# # add element end
# my_list.append(6)
# print(my_list)
# # remove last element
# #popped_item = my_list.append()
# # sort
# new_lists = [4, 2, 1, 8, 5]
# new_lists.sort()
# sorted = new_lists.sort()
# print(sorted)

# # dictionary is unordered and use key value "{"key1":"value1","key2":"value2"}"
# my_dict = {"key1": "value1", "key2": "value2"}
# print(my_dict["key1"])
# # my_dict.keys(),my_dict.value(),my_dict.items()

# # Tuples is like a list but immutability(not change)
# t = (1, 2, 3, 4)

# # I/O Files
# # with open("myfile.txt",mode ="r") as myfile:
# #     content = myfile.read()

# # with open("myfile.txt") as myfile:
# #     content = myfile.read()

myfile = open("myfile.txt")
with open("myfile.txt") as my_new_file:
    contents = my_new_file.read()
print(contents)
