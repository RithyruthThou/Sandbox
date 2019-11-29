"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(determine_grades(score))
def determine_grades(score):
    if score > 100 or score < 0:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    elif score < 50:
        grade = "Bad"
    return grade
main()