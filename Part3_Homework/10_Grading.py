# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

def get_letter_grade(score: float) -> str:
	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	if score >= 60:
		return "D"
	return "F"


def main() -> None:
	try:
		s = input("Enter student's score: ").strip()
		score = float(s)
	except ValueError:
		print("Invalid input. Please enter a numeric score.")
		return

	grade = get_letter_grade(score)
	print(f"Score: {score} -> Grade: {grade}")


if __name__ == "__main__":
	main()