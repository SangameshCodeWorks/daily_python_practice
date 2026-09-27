
#concatination
firstname = "Rajendara"
middlename = "Raja"
lastname = "Cholan"

fullname = firstname +" "+middlename+" "+ lastname

print(fullname)

'''studentname = str(input("enter the Student full name :"))
sage = int(input("enter the student age : "))
smarks = float(input("enter the marks of student :"))
print(f"Student name is :{studentname} and age is {sage} and marks secured is {smarks}")
'''

player = str(input("player name :"))
countryname = str(input("country name :"))
page = int(input("player age :"))
playerheight = float(input("player height :"))
islegend = eval(input("is legend :"))
print(f"{player} plays {countryname} age is {page} and height {playerheight} is a {islegend}")
print("{} plays {} age is {} and height {} is a {}".format(player,countryname,page,playerheight,islegend))
