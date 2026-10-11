scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]


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

def calculate_stats(scores):
    if not scores:
        return {"average": 0, "highest": 0, "lowest": 0}

    return ({
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
        "count": len(scores)
    })

def count_grades(scores):
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for score in scores:
        grades = get_letter_grade(score)
        counts[grades]+=1
    return counts

def display_report(scores):
    stats = calculate_stats(scores)
    grades = count_grades(scores)
    passing = sum(1 for score in scores if score >= 60)
    print("====Grade Report====")
    print(f"Total Score: {stats['count']}")
    print(f"Total Score: {stats['average']}")
    print(f"Highest Score: {stats['highest']}")
    print(f"Lowest Score: {stats['lowest']}")
    print(f"Passing Score: {passing} ({passing / stats['count'] * 100:.0f}%)")
    print("Grade Distribution")
    for grade, count in grades.items():
        print(f"{grade}: {count} students")

print(display_report(scores))

honor_scores = [90, 98, 97, 100, 99, 95]

print(display_report(honor_scores))
