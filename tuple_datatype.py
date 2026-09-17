tup = () # create the tuple using the ()
print(tup)
dt=type(tup) #find the data type of the variable type()
print(dt)

print("-----------------------------------")

# used to show the how many elements are present in the tuple using len()
print(len(tup))
#or
a = len(tup)
print(a)
print("-----------------------------------")

t3 =(11,22,33,54)
dt1=type(t3)
size=len(t3)
print(dt1)
print(size)
print("-----------------------------------")

#t4=(50) if you check the data type of this it gives as int data type but you need it in the tuple so you have to add , comma
#if you want it as the tuple in python 
#we need to place a comma at the end ,when we have the single element
#inside the tuple
t4=(50,)
dt2=type(t4)
print(dt2)
print("-----------------------------------")

t5 = (23,33,4,3,53,63j,True,45.5)
ind=t5[-2]
print(ind)
print(t5)
# t5[6]=100 TypeError: 'tuple' object does not support item assignment because IMMUTABLE
print("-----------------------------------")



