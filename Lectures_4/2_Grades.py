def evaluate(grade: float):
    if 2.0 <= grade <= 2.99:
        return "Fail"
    elif grade <= 3.49:
        return "Poor"
    elif grade <= 4.49:
        return "Good"
    elif grade <= 5.49:
        return "Very Good"
    elif grade <= 6.0:
        return "Excellent"


print(evaluate(float(input())))