result = True
anather_result = result
print(id(result))
print(id(anather_result))

result = False
print(id(result))

result = "hello"
anather_result = result
print(id(result))
print(id(anather_result))