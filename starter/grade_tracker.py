import csv

#Function 1
def load_students(filepath):
    try:
        with open(filepath, newline="") as file: #Looks up the file
            reader = csv.DictReader(file)
            rows = list(reader)
            return rows
    except FileNotFoundError: #I had an extra :(colon) in this line that I had to fix
        print(f"Error: Could not find file: {filepath}")
        return []

#Function 2

def calculate_average(grades):
    valid_grades = []
    for grade in grades:
        if grade != "": #Empty string we skip adding it not an empty string we add it to the list
            valid_grades.append(float(grade))
    if len(valid_grades) == 0: #The first time I ran it I had an indention error here and I fixed it and it ran correctly
        return None  # no valid grades, so there's no average (avoids dividing by 0)
    average = sum(valid_grades) / len(valid_grades)
    return round(average, 1)


#Testing
if __name__ == "__main__":
    students = load_students("data/students.csv")
    print(len(students))
    print(students[1])
    missing = load_students("data/nope.csv")
    print(missing)
    print(calculate_average(["", "79", "81", "76"]))  # expect 78.7