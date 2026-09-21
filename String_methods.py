s1 = "krishan"
print(s1.capitalize())
print("------------------------------------------------")
s2 = "tomarrow is saturday"
print(s2.title())

print("------------------------------------------------")

s3 = "benedict"
print(s3.upper())
print(s3.isupper())

print("------------------------------------------------")

s4 = "TOMARROW IS GANESHA FESTIVAL"
print(s4.lower())

print("------------------------------------------------")

print(s2.islower())
print("------------------------------------------------")

s5 = "Hello Get Lost"
print(s5.startswith("H"))

print("------------------------------------------------")


print("------------------------------------------------")
s6 = ('hahaha')
print(s6.replace('a','e'))

print("------------------------------------------------")

s7 = "Good Morning"
print(s7.swapcase())

print("------------------------------------------------")

s8 = "mahesh04@gmail.com"
print(s8.isalpha())

print("------------------------------------------------")

s9 = "995864733"
print(s9.isdigit())

print("------------------------------------------------")

s10 = "cdds56re122"
print(s10.isalnum())

print("------------------------------------------------")
s11 = "FAAANTAA"
print(s11.count('A'))
print(s11.count("AA"))

print("------------------------------------------------")

print(s11.index('AA'))



#split()method
s12= "Good day everyone how are you"
word=s12.split()
print(word)

print("------------------------------------------------")


s13 = "karthik,durga,shravani"
word2 = s13.split(",")

print(word2)

print("------------------------------------------------")

s14 = "21/09/2026"
word4 = s14.split("/")
print(word4)

print("------------------------------------------------")

l1 = ['apple','mango','banana']
s15=" ".join(l1)
print(s15)

print("------------------------------------------------")

date = ['15','08','1947']
st16="/".join(date)
print(st16)
