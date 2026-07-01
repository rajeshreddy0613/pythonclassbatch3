name = "Dadi"
vowels = "aeiou"
y = name[-1]

for y in vowels:
    name = name[:-1]
    break

name += "k"
print(name)