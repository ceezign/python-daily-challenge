# Grade Calculator Program

def get_scores_from_input(user_input):
    """ Takes a string of scores separated by commas, and validates them, and
    returns alist od valid scores (0 - 100)."""

    scores = []
    for item in user_input.split(","):
        item = item.strip()
        if item.isdigit():
            score = int(item)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print(f" ignored invalid score: {item} (must be 0-100)")
        else:
            print(f" Ignored non-numeric input: {item}")
    return scores

def calculate_average(scores):
    """ Returns the average of scores rounded to 2 decimal places. """
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)

def get_letter_grade(average):
    """ Returns the average of scores rounded to 2 decimal places."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    elif average >= 30:
        return "E"
    else:
        return "F"


def check_pass_fail(average):
    """ Returns "Pass" if average >= 60, otherwise "Fail"."""
    return "Pass" if average >= 60 else "Fail"

def process_student():
    user_input = input("Enter scores separated by commas:")
    scores = get_scores_from_input(user_input)

    if not scores:
        print(" NO VALID SCORES ENTERED!")
        return None

    avg = calculate_average(scores)
    grade = get_letter_grade(avg)
    status = check_pass_fail(avg)

    print("\nSTUDENT RESULT")
    print("------------")
    print(f"Scores Entered : {scores}")
    print(f"Average Scores: {avg}")
    print(f"Letter Grade : {grade}")
    print(f"Status     : {status}")
    print("------------")

    return {"Scores": scores, "Average": avg, "Grade": grade, "Status": status }

def main():
    results = []
    while True:
        student_result = process_student()
        if student_result:
            results.append(student_result)

        again = input("Do you want to enter another student? (y/n): ").lower()
        if again != "y":
            break

    with open("Student_result.csv", "w") as file:
        file.write("Scores,Average,Grade,Status\n")
        for r in results:
            file.write(f"{r['Scores']},{r['Average']}, {r['Grade']},{r['Status']}\n")
    print("\n All Results saved to student_result.csv")

if __name__ == "__main__":
    main()
