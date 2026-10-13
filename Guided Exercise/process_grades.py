import csv

#Read Student Data
#My Headers start with a Capital Letter

students = []

with open('students.csv', 'r',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Score"] = int(row['Score']) #Convert Score to int and store the full record
        students.append(row)

print(f"Loaded {len(students)} students records.")

#Group Scores by Subject

subjects = {}
for student in students:
    subject = student["Subject"]
    if subject not in subjects:
      subjects[subject] = []
    subjects[subject].append(student["Score"])

print("\n=== Subject Averages ===")
for subject, scores in subjects.items():
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.1f} ({len(scores)} students)")



#Write results to a text file

all_scores = [s["Score"] for s in students]

with open("grade_report.txt", "w") as file:
    file.write("GRADE REPORT\n")
    file.write("=" * 40 +"\n \n")
    file.write(f"Total Students: {len(students)}\n")
    file.write(f"Overall Average: {sum(all_scores)/len(all_scores):.1f}\n")
    file.write(f"Highest Score: {max(all_scores)}\n")
    file.write(f"Lowest Score: {min(all_scores)}\n")

    file.write("BY SUBJECT:\n")
    for subject, scores in subjects.items():
        avg = sum(scores) / len(scores)
        file.write(f"{subject}: {avg:.1f} ({len(scores)} students)\n")

print("\nReport written to: grade_report.txt")

#Add letter grades and write to new CSV

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

with open("students_graded.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Score", "Subject", "Grade"])
    writer.writeheader()

    for student in students:
        student["Grade"] = get_letter_grade(student["Score"])
        writer.writerow(student)

print("Graded data written to students_graded.csv")
