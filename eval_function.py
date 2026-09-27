a = 10
b = 20
l = [11,22,33]

result = eval("a+b+(len(l))")
print(result)

result1 = eval("{22,33,66}")
print(type(result1))
print(result1)


result2 = eval("False")
print(type(result2))
print(result2)
