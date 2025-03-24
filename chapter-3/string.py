# name="Amara"
# nameshort=name[0:3]#start from index 0 and print characters till index 2 means 'Ama'
# print(nameshort)
# char1=name[1]
# print(char1) #print character at index 1 that is 'm'
#       #        ...........................................

# # Negative slicing
# name1="Muzamil"
# print(name1[-7:-1]) #means  -7=0,-6=1,-5=2,-4=3,-3=4,-2=5,-1=6
# print(name1[1:6])
# print(name1[:6]) #means 0:6
# print(name1[2:]) #means 2:6
#       #              ...........................................
# name2="0123456789"
# print(name2[1:7:3]) #first it will select 1:7 characters then from this like '1234567'
# #then from thisn'1234567' it will go beyond 1 until 3 that is 4
#       #              ...........................................

# String function
# name="haris"
# print(len(name)) #lenght of name
# print(name.endswith("ris"))#does the name  end with ris
# print(name.endswith("yris"))#does the name  end with yris
# print(name.startswith("ha"))#does the name  start with ha
# print(name.startswith("Ha"))#does the name  start with Ha
# #there are many string functions you can ask from chatgpt  or
#  # browse from google
#       #              ...........................................

#Escape sequence
# a="Amara is girl \n not a boy"
# print(a)

#       #              ...........................................

#f string
# a=input("Enter name:")
# print(f"Good Afternoon {a}") #with the use of f string you can write
# #variable {a} with the string
#       #              ...........................................

# Q=Replace  name with youer name or date with date?
# letter='''Dear <|Name|>
# You are selected!
# <|Date|>'''
# print(letter.replace("<|Name|>","Amara").replace("<|Date|>","2/8/2025"))
#       #              ...........................................

# Find occurence of substring 
# name="Amara is a girl"
# print(name.find("is")) #It will give output 6 means is at 6 position
# print(name.find("  ")) #It will give output -1 means there is no double space
#       #              ...........................................

#Replace doble space with single space
name="Amara is a  girl"
print(name.replace("  "," "))
print(name) #string are immutable means you cannot change orignal 
# #string you just apply function on stirng which creates new string
#       #              ...........................................


