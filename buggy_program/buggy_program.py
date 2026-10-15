# buggy_program.py — Contains 4 bugs. Find and fix them all.

def calculate_stats(numbers): #There was no colon at the end of this line
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    above_average = []
    for num in numbers:
        if num > average: #No colon at the end of this line
            above_average.append(num)

    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }


scores = [85, 92, 78, 95, 88, 70, 93] #70 was a string not an int I removed the ""
result = calculate_stats(scores)

print(f"Total: {result['total']}")
print(f"Average: {result['average']}")# average was not in quotes and giving a undefined error I added ''
print(f"Above average: {result['above_count']} scores")