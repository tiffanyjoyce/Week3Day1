import re
with open("regex_test.txt") as file:
    data = file.readlines()
    print(data)
    
#     names_pattern = re.compile("([A-Za-z]+) ([A-Za-z]+) ([A-Za-z]$)")
#     name_found = names_pattern.findall(data)
#     print(name_found)


# print(data.split(","))
# for name in data.split(","):
#     match = names_pattern.search(name)

#     if match:
#         print(match.group())
#     else:
#         print("None")