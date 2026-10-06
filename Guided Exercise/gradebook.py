# gradebook.py - A simple student gradebook using lists

#Students names and their test scores

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

scores = [88, 75, 95, 82, 91]

print("=" * 35)
print("      Student Gradebook")
print("=" * 35)

# Display all students and scores

for i in range(len(students)):
    print(f"{students[i]:<12} {scores[i]}")
# Calculate class stats

total = sum(scores)  #Built-in function that adds all items

average = total / len(scores) #Total divided by count

highest = max(scores)

lowest = min(scores)

print("-" * 35)
print(f"Class Average: {average:.1f}")
print(f"Class Highest: {highest:.1f}")
print(f"Class Lowest:  {lowest:.1f}")

# Find the student with the highest score

highest_index = scores.index(highest)
top_student = students[highest_index]

print(f"Top Student: {top_student} ({highest})")

#Add a new student

print("\n--- Adding a new student ---")
new_name = input("Students Name: ")

try:
    new_score = int(input("Test score: "))
except ValueError:
    print("Invalid input. 0")
    new_score = 0

students.append(new_name)
scores.append(new_score)

#Recalculate and display

new_average = sum(scores) / len(scores)
print(f"\n Updated Roster: {len(students)} students")
print(f"New Class average: {new_average:.1f}")

#Sort a copy of scores (don't modify the original)

sorted_scores = sorted(scores) #sorted() returns a new sorted list

#Find the median

mid = len(sorted_scores) // 2 #//is integer division (no decimal)

if len(sorted_scores) % 2 == 0:
    median = (sorted_scores[mid - 1] + sorted_scores[mid]) / 2

else:
    median = sorted_scores[mid]
print(f"Median Score: {median}")
















