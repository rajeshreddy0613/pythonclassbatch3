# Dictionary setup
# 1. Create a dictionary for a student with name, age, and grade.
student = {
    "name": "Rajesh",
    "age": "26",
    "grade": "A"
}

marks = {"scores": [50, 65, 75, 85, 90]}
scores = [50, 65, 75, 85, 90]

# 2. Print all keys in the dictionary.
print(student.keys())

# 3. Print all values in the dictionary.
print(student.values())

# 4. Add a new key "city" with value "Austin".
student["city"] = "Austin"   
print(student)

# 5. Update the student's age.
student.update({"age": "24"})  
print(student)

# 6. Remove a key from the dictionary.
student.pop("city")  
print(student)

# 7. Count the number of key-value pairs without using len().
count = 0
for x in student:
    count = count + 1
print(count)

# 8. Find the highest score.
max_value = scores[0]
for x in scores:
    if x > max_value:
        max_value = x
print(max_value)

# 9. Calculate the average score.
total = 0
for num in scores:
    total = total + num
print(total)
print(len(scores))
cal = total / len(scores)
print(cal)

# 10. Print only students scoring above 90.
for y in scores:
    if y >= 90:       
        print(y)