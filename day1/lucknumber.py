def get_student_result(avg_score):
    if not isinstance(avg_score, (int, float)) or avg_score < 0 or avg_score > 100:
        return "Invalid input. Please enter a score between 0 and 100."
    
    if 0 <= avg_score <= 49:
        return "Fail"
    elif 50 <= avg_score <= 74:
        return "SC"
    elif 75 <= avg_score <= 90:
        return "FC"
    elif 91 <= avg_score <= 100:
        return "Distinction"

# Example usage
avg_score = float(input("Enter the average score: "))
result = get_student_result(avg_score)
print(result)
