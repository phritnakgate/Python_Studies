#ค้นหา+นับอักษร
message = ["aa", "aab", "cba", "bba", "abb", "cca"]
result=[]
for item in message:
    result.append(item.count("a"))
print(result)