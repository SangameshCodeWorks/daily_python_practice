sangu = [101,102,103,104,108]
#var = type(sangu)
#print(var)
print(sangu)
sangu.append(110)
print(sangu)

sangu.insert(1,51)
print(sangu)
print("----------------------------------------------")

l2 = [10,20,30,50,60]
l2.insert(-10,100)
print(l2)
print("----------------------------------------------")

print("combining the two list using extend method, in existing the list")

sangu.extend(l2)
print(sangu)
print("-----------------------------------------------")
print("concatination of list it creates the new list called list04 to combine the sangu and l2")
list04=sangu+l2
print(list04)
print("-----------------------------------------------")


print("removing the last element using pop method")
l5=[21,22,23,24]
rem_ele=l5.pop()
print(rem_ele)
print(l5) 
print("-----------------------------------------------")

print("removing the last element using pop method initializing the index number")
l5.pop(2)
print(l5)
print("-----------------------------------------------")

print("removing the first reoccring element  using remove method by giveing the direct element without index number")
l7 = [99,98,94,95,92,93,98,100]
print("before:",l7)
l7.remove(98)
print("After:",l7)
print("-----------------------------------------------")

#reverse
l8 = [11,22,33,44]
l8.reverse()
print(l8)
print("-----------------------------------------------")

#sort
l9 = [4,6,1,9,7,3,2,8]
l9.sort()
print(l9)
print("-----------------------------------------------")

#count
l10 = [33,11,45,11,32,11,33,55,45,55,11]
cou=l10.count(11)
print(cou)
print("-----------------------------------------------")

#index
l11 = [33,11,45,11,32,11,33,55,45,55,11]
ind=l11.index(11)
print(ind)
print("-----------------------------------------------")

#sum of the smallest and the largest number in the list

l = [59,12,18,14,17]
l.sort()
sum = l[0] + l[-1]
print(l)
print(sum)


