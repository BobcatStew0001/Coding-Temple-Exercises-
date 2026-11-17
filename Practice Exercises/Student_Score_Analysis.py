import pandas as pd


data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}
df = pd.DataFrame(data)

# Part 1
print("--Student per Course--")
course_totals = df["course"].value_counts()
print(course_totals)

# Part 2
print("--Avg Score per Course--")
avg_score = df.groupby("course")["score"].mean()
print(avg_score)

# Part 3
print("--Top 3 by Score--")
top_three = df.nlargest(3, ["score"])
print(top_three)

# Part 4
print("--Avg Hours Studied--")
avg_hours = df.groupby("passed")["hours_studied"].mean()
avg_hours.index = avg_hours.index.map({True:"Passed", False:"Failed"})
print(avg_hours)

# Part 5
print("--New Grade Column--")
def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

df["grade"] = df["score"].apply(letter_grade)
print(df)

# Part 6
print("--Grades by Course--")
grades_by_course = pd.crosstab(df["course"], df["grade"])
print(grades_by_course)