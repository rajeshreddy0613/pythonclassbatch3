import random

names = ["Tirumal", "Pavan", "Manasa", "Rajesh", "Suresh", "Priya", "Kiran"]

print(random.choice(names))
# 1. Create a list of 5 fruits and print all items.
fruits=["Apple","PineApple", "Gauva","Banana","Orange"]
print(fruits)

# 2. Add "Mango" to the end of the list.
fruits.append("Mango")
print(fruits)

# 3. Remove "Banana" from the list.
fruits.remove("Banana")
print(fruits)

# 4. Find the length of a list without using len().
fruits=["Apple","PineApple", "Gauva","Banana","Orange"]
count = 0
for fruit in fruits:
   count = count + 1
print(count)
  
# 5. Print all elements using a for loop.
fruits=["Apple","PineApple", "Gauva","Banana","Orange"]
for fruit in fruits:
   print(fruit)

# 6. Find the largest number in a list without using max().
fruits=["Apple","PineApple", "Gauva","Banana","Orange"]

max_fruit=fruits[0]
   
for x in fruits:
     if x > max_fruit:
         max_fruit= x
    
print(max_fruit)


# 7. Find the smallest number in a list without using min().
fruits=["Apple","PineApple", "Gauva","Banana","Orange"]

min_fruit=fruits[0]
   
for x in fruits:
     if x < min_fruit:
            min_fruit=x
    
print(min_fruit)


# 8. Count how many times a number appears in a list.
fruits = ["Apple", "PineApple", "Guava", "Banana", "Orange", "Apple"]

target = "Apple"
count = 0

for fruit in fruits:
    if fruit == target:
        count = count + 1

print("Count of", target, ":", count)

# 9. Create a new list containing squares of numbers.

numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# 10. Reverse a list without using reverse().
fruits = ["Apple", "PineApple", "Guava", "Banana", "Orange"]

reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruits:", reversed_fruits)

