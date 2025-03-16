def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def display_records(records):
    print("Student Records:")
    print("{:<15} {:<10} {:<5}".format("Name", "Score", "Grade"))
    print("-" * 30)
    for record in records:
        name, score = record[0], record[1]
        grade = calculate_grade(score)
        print("{:<15} {:<10} {:<5}".format(name, score, grade))
    print("\n")

def main():
    # Initializing student records as tuples (name, score)
    student_records = [
        ("Poushali", 85),
        ("Ayan", 92),
        ("Pritha", 78),
        ("Debanjan",50),
        # Add more records as needed
    ]

    display_records(student_records)

if __name__ == "__main__":
    main()
