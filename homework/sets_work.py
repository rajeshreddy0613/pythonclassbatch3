#create a set
colors={"orange", "blue", "green", "black", "brown"}
print(colors)
#add yellow
colors.add("yellow")
print(colors)
# remove blue
colors.remove("blue")
print(colors)
# check green exist or not
for x in colors:
    if(x =="green"):
     print("True")
# print all elements using loop
for y in colors:
   print(y)     
# create a new set
colors2={"green","blue","white"}  
print(colors2)
# intersection of two sets (common)&
colors3=colors.intersection(colors2)
print(colors3)
# unique element of two sets ^
colors3=colors.symmetric_difference(colors2)
print(colors3)
# union of two sets
colors3=colors|colors2
print(colors3)
# difference of two sets
colors3=colors-colors2
print(colors3)


