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

def get_letter_grade(average):
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_report(students):
    results = []
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}

    for student in students:
        grades = [student["math"], student["science"], student["english"], student["history"]]
        average = calculate_average(grades)
        letter = get_letter_grade(average)
        results.append({"name": student["student_name"], "average": average, "grade": letter})
        distribution[letter] += 1

    valid_averages = [r["average"] for r in results if r["average"] is not None]

    if valid_averages:
        class_average = round(sum(valid_averages) / len(valid_averages), 1)
        highest = max(valid_averages)
        lowest = min(valid_averages)

    else:
        class_average = highest = lowest = None

    return {
        "total_students": len(students),
        "class_average": class_average,
        "highest_average": highest,
        "lowest_average": lowest,
        "grade_distribution": distribution,
        "students": results,}

def write_report(report, filepath):
    with open(filepath, "w") as file:
        file.write('=' * 40 + "\n")
        file.write(f"{'Student Grade Report':^40}\n")
        file.write(f"{'Created by Zach Brown':^40}\n")
        file.write('=' * 40 + "\n\n")
        file.write('=' * 40 + "\n")
        file.write(f"{'Summary':^40}\n")
        file.write('=' * 40 + "\n")
        file.write(f"Total Students: {report['total_students']}\n")
        file.write(f"Class Average: {report['class_average']}\n")
        file.write(f"Highest Average: {report['highest_average']}\n")
        file.write(f"Lowest Average: {report['lowest_average']}\n\n")

        file.write('=' * 40 + "\n")
        file.write(f"{'Grade Distribution':^40}\n")
        file.write('=' * 40 + "\n")
        for letter, count in report["grade_distribution"].items():
            file.write(f"{letter}: {count}\n")
        file.write('\n')

        file.write('=' * 40 + "\n")
        file.write(f"{'Top 5 Students':^40}\n")
        file.write('=' * 40 + "\n")
        graded = [s for s in report["students"] if s["average"] is not None]
        top_five = sorted(graded, key=lambda s: s["average"], reverse=True)[:5]
        for rank, student in enumerate(top_five, start=1):
            file.write(f"{rank}. {student['name']:<20} {student['average']:>6} {student['grade']}\n")
        file.write('\n')

        file.write('=' * 40 + "\n")
        file.write(f"{'Individual Results':^40}\n")
        file.write('=' * 40 + "\n")
        for student in report["students"]:
            average = student["average"] if student["average"] is not None else "N/A"
            file.write(f"{student['name']:<20} {average:>6} {student['grade']}\n")













#Testing
def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")

    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")
    sorted_students = sorted(
        [s for s in report["students"] if s["average"] is not None],
        key=lambda s: s["average"],
        reverse=True
    )
    for s in sorted_students[:5]:
        print(f"  {s['name']:<20} {s['average']:.1f}  ({s['grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()