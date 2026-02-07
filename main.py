import re
import datetime

print("    SMART STUDY PLANNER     ")

# --------------------------
# Student Details
# --------------------------
print("\nEnter Student Details:")
# Student name input with validation
while True:
    student_name = input("Name: ").strip()
    if student_name == "":
        print("Name cannot be empty.")
    elif not all(c.isalpha() or c.isspace() for c in student_name):
        print("Name can only contain letters and spaces.")
    else:
        break


# Graduation Year validation
current_year = datetime.datetime.now().year
while True:
    grad_year = input("Graduation Year: ").strip()
    if not grad_year.isdigit():
        print("Enter a valid 4-digit year.")
    elif len(grad_year) != 4:
        print("Year must be 4 digits.")
    elif int(grad_year) < current_year:
        print("Graduation year cannot be in the past.")
    else:
        grad_year = int(grad_year)
        break
        

while True:
    email = input("Email ID: ").strip()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        break
    else:
        print("Enter a valid email address.")


# --------------------------
# Daily Study Hours
# --------------------------
while True:
    try:
        weekday_hours = float(input("Enter available study hours per weekday: "))
        weekend_hours = float(input("Enter available study hours per weekend day: "))
        if weekday_hours >= 0 and weekend_hours >= 0:
            break
        else:
            print("Hours must be positive numbers.")
    except ValueError:
        print("Please enter valid numbers.")

# --------------------------
# Number of Subjects
# --------------------------
num_subjects = int(input("\nHow many subjects do you want to plan for? "))
print(f"You want to plan for {num_subjects} subjects.\n")

# --------------------------
# Initialize Lists / Dicts
# --------------------------
subjects = []
difficulty = {}
deadlines = {}

# --------------------------
# Input Loop for Subjects
# --------------------------
for i in range(num_subjects):
    while True:
        subject = input(f"Enter subject {i+1} name: ").strip()
        if subject not in subjects:
            subjects.append(subject)
            break
        else:
            print(f"{subject} already entered, please enter a new subject.")

    while True:
        try:
            diff = int(input(f"Enter difficulty for {subject} (1-5): "))
            if 1 <= diff <= 5:
                difficulty[subject] = diff
                break
            else:
                print("Difficulty must be 1-5.")
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            ddl = int(input(f"Enter deadline for {subject} (days left): "))
            if ddl > 0:
                deadlines[subject] = ddl
                break
            else:
                print("Deadline must be positive.")
        except ValueError:
            print("Enter a valid number.")

# --------------------------
# Step 3: Calculate Priority
# --------------------------
priorities = {subject: difficulty[subject]/deadlines[subject] for subject in subjects}

# Emergency boost for near deadlines
for subject in priorities:
    if deadlines[subject] <= 2:
        priorities[subject] *= 1.5

# Total priority and available hours
total_priority = sum(priorities.values())
total_available_hours = weekday_hours*5 + weekend_hours*2

# Estimated hours
estimated_hours = {subject: round((priorities[subject]/total_priority)*total_available_hours, 1) for subject in subjects}

# Cognitive load adjustment: reduce hours for very hard subjects
for subject in estimated_hours:
    if difficulty[subject] >= 5:
        estimated_hours[subject] = round(estimated_hours[subject]*0.9, 1)

# --------------------------
# Step 4: Print Collected Data
# --------------------------
print("\nCollected Subjects and Deadlines:")
for subject in subjects:
    print(f"{subject}: Difficulty={difficulty[subject]}, Deadline={deadlines[subject]}")

# --------------------------
# Step 5: Print Smart Plan
# --------------------------
print("\nGenerating Your Smart Plan:")
print(f"{'Subject':<15}{'Difficulty':<10}{'Deadline':<10}{'Est. Hours':<10}")

for subject in sorted(subjects, key=lambda x: priorities[x], reverse=True):
    print(f"{subject:<15}{difficulty[subject]:<10}{deadlines[subject]:<10}{estimated_hours[subject]:<10}")

# Optional: Show student info
print(f"\nPlan for: {student_name}, Graduation Year: {grad_year}, Email: {email}")
