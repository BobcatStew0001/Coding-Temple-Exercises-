    #  Step 1) Uses a for loop to iterate through the scores and categorize each one:
        # 90-100: "A"
        # 80-89: "B"
        # 70-79: "C"
        # 60-69: "D"
        # Below 60: "F"
    # Step 2) Counts how many students are in each letter grade category
    # Step 3) Calculates and displays:
        # Total number of scores
        # Average score (formatted to 1 decimal)
        # Highest and lowest score
        # Number of passing scores (60+) and failing scores (below 60)
        # The distribution of letter grades
    # Step 4) Uses a while loop to let the user enter additional scores. After each entry, display the updated average. Stop when the user types "done".

    # Starts with this list of student scores:
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
divider = '-' * 10

while True:
    #Step 1
    score_a = list()
    score_b = list()
    score_c = list()
    score_d = list()
    score_f = list()

    for score in scores:
        if score <= 100 and score >= 90:
            score_a.append(score)
        elif score >= 80 and score <= 89:
            score_b.append(score)
        elif score >= 70 and score <= 79:
            score_c.append(score)
        elif score >= 60 and score <= 69:
            score_d.append(score)
        else:
            score_f.append(score)
    #Step 2
    count_a = len(score_a)
    count_b = len(score_b)
    count_c = len(score_c)
    count_d = len(score_d)
    count_f = len(score_f)

    #Testing to make sure the code runs and output is correct
    print(f"A's:{score_a}, B's:{score_b}, C's:{score_c}, D's:{score_d}, F's:{score_f}")
    print(f"A's: {count_a}, B's: {count_b}, C's: {count_c}, D's: {count_d}, F's: {count_f}")

    print(divider)

    #Step 3
    total_scores = len(scores) #Total number of scores
    sum_scores = sum(scores) #Total value of scores
    avg_scores = sum(scores) / len(scores) #Average of scores
    #Store Passing & Failing scores
    pass_score = list()
    fail_score = list()

    for score in scores:
        if score >= 60:
            pass_score.append(score)
        else:
            fail_score.append(score)
    #Highest & Lowest Scores
    max_score = max(scores)
    min_score = min(scores)

    #Testing to make sure the code runs and output is correct
    print(f"The total number of scores is: {total_scores}")
    print(divider)
    print(f"Sum of the scores: {sum_scores}")
    print(divider)
    print(f"The average score is: {avg_scores:.1f}")
    print(divider)
    print(f"All passing scores: {pass_score}")
    print(f"All failing score: {fail_score}")
    print(divider)
    print(f"Total passing scores: {len(pass_score)}")
    print(f"Total failing score: {len(fail_score)}")
    print(divider)
    print(f"Max score: {max_score}")
    print(f"Min score: {min_score}")
    # Step 4
#Tested 3 times: 32, 98, t9 and program performed as expected.
    try:
        user_score = input("Please enter a number or 'done' to finish: ").strip().lower()
        if user_score == "done":
            print("Finished entering scores")
            break
        else:
            new_score = int(user_score)
            scores.append(int(user_score))
            updated_avg = sum(scores) / len(scores)
            print(f"Score added! Updated average score is {updated_avg:.1f}")
            print(divider)
            print(f"Max score: {max_score}")
            print(f"Min score: {min_score}")
            print(divider)

    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")







