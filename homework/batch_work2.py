# 1. Create a tuple of 5 numbers
numbers = (10, 11, 12, 13, 14)
print(numbers)

# 2. Print the first and last element
numbers = (10, 11, 12, 13, 14)
print(numbers[0])
print(numbers[-1])

# 3. Count the number of elements without using len()
numbers = (10, 11, 12, 13, 14)
count = 0
for x in numbers:
    count = count + 1
print(count)

# 4. Find the maximum value in a tuple
numbers = (10, 11, 12, 13, 14)
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(max_value)

# 5. Find the minimum value in a tuple
numbers = (10, 11, 12, 13, 14)
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print(min_value)

# 6. Count occurrences of a value
numbers = (10, 11, 10, 12, 13)
target = 10
count = 0
for num in numbers:
    if num == target:
        count = count + 1
print(count)

# 7. Convert a tuple into a list
numbers = (10, 11, 12, 13, 14)
my_list = list(numbers)
print(my_list)

# 8. Convert a list into a tuple
my_list = [10, 11, 12, 13, 14]
numbers = tuple(my_list)
print(numbers)

# 9. Unpack a tuple
numbers = (10, 11, 12)
a, b, c = numbers
print(a)
print(b)
print(c)

# 10. Find the sum of all numbers in a tuple
numbers = (10, 11, 12, 13, 14)
total = 0
for num in numbers:
    total = total + num
print(total)