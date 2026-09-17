#add method in sets
s3 = set()
s3.add(32)
s3.add(41)
s3.add(5)
print(s3)
print("----------------------------------------")

#updateing the existing set by using the update Method
s2 = {11,22,33}
s3.update(s2)
print(s3)

print("----------------------------------------")
#pop method
s4 = {23,24,25,26}
ele=s4.pop()
print(s4)
print(ele)

print("----------------------------------------")
#remove Method
s5 ={7,8,9,5}
s5.remove(8)
#s5.remove(18)
print(s5)

#discard Method
s5.discard(50)
print(s5)

print("----------------------------------------")
#clear method, delete all the elements from the set and it will make it empty
s5.clear()
print(s5)

print("----------------------------------------")
#issubset method
s6 = {9,10,11}
s7={21,10,22,9,11}
bv1=s6.issubset(s7)
print(bv1)
#issuperset method
bv2=s7.issuperset(s6)
print(bv2)


print("----------------------------------------")
#isdis joint if same elements in diffrent set when comparing by suing disjoint i will show false
s8 = {88,77,66}
s9={66,55,44}
bv3=s8.isdisjoint(s9)
print(bv3) 

print("----------------------------------------")

#union method it combine all  elements of both set except duplicates it taken only once
s10 = {12,13,14}
s11 = {14,15,16}
us=s10.union(s11)
print(us)
#intersection returns only duplicate value
inter=s10.intersection(s11)
print(inter)

#diffrence
ds=s10.difference(s11)
print(ds)

#symetric diffrence gives uncomman elements of both set
sd=s10.symmetric_difference(s11)
print(sd)
print("----------------------------------------")

