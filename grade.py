# Simple Student Grade Tracker 📚
# A beginner-friendly program to store and view student grades

# Initialize simple lists to store data
names = []  # List for student names
scores = []  # List for student scores
grades = {}  # Dictionary to link names with grades
top_students = set()  # Set for students with score >= 90

print("Welcome to Simple Grade Tracker! 📚")

while True:
    # Simple Menu
    print("\n=== Menu ===")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("\nWhat would you like to do? (1/2/3): ")

    # 1. Adding a new student
    if choice == "1":
        # Get student name
        name = input("\nEnter student name: ").title()

        # Get score (with simple error checking)
        while True:
            try:
                score = float(input("Enter score (0-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("Please enter a score between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")

        # Store data
        names.append(name)
        scores.append(score)

        # Store in dictionary
        grades[name] = score

        # Check if it's a top score
        if score >= 90:
            top_students.add(name)

        print(f"\n✨ Added {name} successfully!")

    # 2. Showing all students
    elif choice == "2":
        if len(names) == 0:
            print("\nNo students added yet!")
        else:
            print("\n=== Student Grades ===")

            # Loop through names and show grades
            for name in names:
                score = grades[name]
                stars = "🌟" if name in top_students else ""
                print(f"{name}: {score} {stars}")

            # Show simple class average
            average = sum(scores) / len(scores)
            print(f"\nClass Average: {average:.1f}")
            print(f"Top Students: {len(top_students)}")

    # 3. Exit program
    elif choice == "3":
        print("\nThanks for using Grade Tracker! 👋")
        break

    # Invalid choice
    else:
        print("\nPlease enter 1, 2, or 3!")
