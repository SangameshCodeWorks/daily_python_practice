print("#*********list creation and its methods*******")
l1 = [20,35,"raj",35.2,True,33j,20]
l2 = [35,36,20,466,20]

    #append(object) Method add the key at the end of the list
l1.append(100)
print(l1)
    #extend it will joins the 2 list
l1.extend(l2)
print(l1)
    #insert(i,object) it add the new value to given index
l1.insert(1,10)
print(l1)
    #pop it will delete the last element or value
l1.pop()
print(l1)
    #remove(object) method it removes the particular object
l1.remove(35)
print(l1)
    #count(object) it will count how many time the object is repeted
print(l1.count(20))
    #index(object) it will returns first occaring the index of the given object
ind=l1.index(20)
print(ind)
    #reverse it will reverse the whole list
l1.reverse()
print(l1)
    #clear it will delete all the elements from the list
l1.clear()
print(l1)
print("************************************************************************************")


print("#*********sets creation and its methods*******")

s1={4,7,9,3,8,2,12,11}
s2={12,15,11,19,10,9,3}

    #add(object) method it will add the object at the any where
s1.add(90)
print(s1)
    #update combines both the set1 and set2
s1.update(s2)
print(s1)
    #pop it removes the any one element from the set
val=s1.pop()
print(s1,val)
    # remove(object) it remove the particular object from the set
s1.remove(90)
print(s1)
'''s1.remove(99)
        print(s1)
        Traceback (most recent call last):
          File "F:/CodePlayground/Python Workspace/ALLdatatypesPractice.py", line 49, in <module>
            s1.remove(99)
                KeyError: 99'''
    #discard(object) as same as remove but it wont return the error iff the given element is not present in set
s1.discard(99)
print(s1)
    #issubset check it the subset of set 2
val2=s1.issubset(s2)
print(val2)
    #issuperset check s1 is super set of set2
val3=s1.issuperset(s2)
print(val2)
    #isdisjoint it checks is the any comman element is there means returns false
val4=s1.isdisjoint(s2)
print(val4)
    #union it add the both the set and duplicate elements only one time
val5=s1.union(s2)
print(val5)

s3= {33,44,55,66}
s4= {55,66,77,88}
    #intersection it will return only comman elements
val6=s3.intersection(s4)
print(val6)

s3= {33,44,55,66}
s4= {55,66,77,88}
    #difference it will return the elements of set1 without comman elements is present in both side
val8=s3.difference(s4)
print(val8)
    #symmetric_diffrence it will return both set elements without comman elements
val9=s3.symmetric_difference(s4)
print(s4)

print("************************************************************************************")

print("#*********Dictionary creation and its methods*******")

d1 = {
    'name1':"sangamesh",
    'age1':22,
    'city1':"bangalore",
    'exp1': 2.5,
    'course1':"python fullstack"}


d2 = {
    'name':'vishwa',
    'age' : 23,
     'city': 'gulbarga',
     'exp' : 3.2,
    'course': 'data science'}


print("                                     .                                   ")

    #setdefault adding the item to the dictionary
d1.setdefault('ispass',True)
print(d1)

    #update method it combines the both dictionary
d1.update(d2)
print(d1)

    #get(key) method it access the particular key and value
value=d1.get("course")
print(value)

    #popitem it only delete the last item  from the dictionary
d1.popitem()
print(d1)

    # pop(key) it remove the particular item from the dictinary
d1.pop("age")
print(d1)

print("                                     .                                   ")

    #keys gives only keys from the dictionary in the form of list
val11=d1.keys()
print(val11)

print("                                     .                                   ")

    #values gives only values from the dictionary in the form of list
val12=d1.values()
print(val12)

print("                                     .                                   ")

    #items it returns all the items in the form of tuples inside the list
val13=d1.items()
print(val13)

print("                                     .                                   ")

    #clear
d2.clear()
print(d2)

print("************************************************************************************")

print("#*********STRINGS creation and its methods*******")

st1 = "sanGamesh jaiNapur mail @123"
st2 = "sanGamesh jaiNapur mail @123"
st3 = "  sanGamesh jaiNapur mail @123  "

    #capitalize it make the first latter of the word is capital letter
st1=st1.capitalize()
print(st1)

    #title it makes the every word first latter in capital letter of the sentance
st1=st1.title()
print(st1)

    #upper make all the letter in upper case
st1=st1.upper()
print(st1)

    #isupper make all the letter in upper case or not it will check TRUE/FALSE
st1=st1.isupper()
print(st1)

    #lower make all the letter in lower case
st2=st2.lower()
print(st2)

    #islower make all the letter in lower case or not it will check TRUE/FALSE
st2=st2.islower()
print(st2)

    #startswith("") it checks is the string starting with this or not
st=st3.startswith("sanG")
print(st)
print(st3)

  #endswith("") it checks is the string endinging with this or not
st=st3.endswith("@123")
print(st)
print(st3)

    #replace("","") it replace the given string with the exixting string 
st = st3.replace("a","e")
print(st)

    #swapcase() it converts the upper case to lower to upper
st=st3.swapcase()
print(st)

    #isalpha it checks only is there only alphabets in the string
st=st3.isalpha()
print(st)

    #isdigit it checks only is there only alphabets in the string
st=st3.isdigit()
print(st)

    #isalnum it checks only is there only alphabets in the string
st=st3.isalnum()
print(st)

    #count("") it tell how many times the string is present
st=st3.count('a')
print(st)

    #index("") first occuring position of th string
st=st3.index('l')
print(st)

    #lstrip() it removes the left side space only
st=st3.lstrip()
print(st)

    #rstrip() it removes the right side space only
st=st3.rstrip()
print(st)

    #strip() removes the space in from right and left
st=st3.strip()
print(st)

st4="0123456789012345678901234567890"
    #sclice means [start:end]Start = start,ends =end+1
print(st4[:8]) #from the postion 8 onword it wont print any thing
print(st4[5:]) # it leaves first 4 numbers ,5 and after that it will print
print(st4[6:25]) #it print position number 6 to 24 , 25  will not print i told first end =end+1
print(st4[::2]) #it prints only 0 2 4 because it skips one place
