# setdefault

d= {}
d.setdefault(11,200)
d.setdefault(22)
d.setdefault(22,400)
print(d)

print("--------------------------------------")

#update it combines the bothe dictionary
d1= {11:12,13:14,15:16}
d2={22:33,44:55,66:77}
d1.update(d2)
print(d1)

print("--------------------------------------")

#get method it access the particular key of the value
d2={22:33,44:55,66:77}
val1=d2.get(44)
val2=d2.get(88)
print(val1)
print(val2)

print("--------------------------------------")

#pop it will delete the particular key and value
d5= {12.4:124,13.5:135}
pv=d5.pop(13.5)
print(pv)
print(d5)

print("--------------------------------------")

d6={1:4,5:7,6:8,2:3}
val3=d6.popitem()
print(val3)
print(d6)


print("--------------------------------------")

ks=d6.keys()
print(ks)

print("--------------------------------------")

vs=d6.values()
print(vs)

print("--------------------------------------")

it=d6.items()
print(it)

print("--------------------------------------")
