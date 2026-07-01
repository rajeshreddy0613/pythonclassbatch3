name = "Dadi"
vowels = "aeiouAEIOU"
y = name[-1]

for y in vowels:
    name = name[:-1]
    break

name += "k"
print(name)