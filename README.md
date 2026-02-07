# Smart-Adaptive-Study-Planner
Smart Adaptive Study Planner that prioritizes subjects based on difficulty and deadlines, helping students study efficiently and reduce mental stress.

## overview
This is a simple, adaptive study planner designed for students to prioritise subjects based on **difficulty and upcoming deadlines**.
The planner helps to reduce mental stress generating a clear, actionable study order.

Even though this is a minimal MVP, it demonstrates** adaptive prioritization logic** and can be extended to include 
student details, study hours, and confidence levels.

## features
- Input subjects, difficulty level(1-5), and deadline(days left)
- Generates a **priority-based study plan**
- Highest priority subjects (hardest + nearest dadline) appear first
- Simple, transparent logic for easy understanding
- Work fully in Python

## How to run
1. open 'main.py' in Python(Replit or local Python environment)
2. Run the program
3. FOllow input prompts:
       -Number of subjects
       -Name of each subject
       -Difficulty(1-5)
       - Deadline (days left until exam)
4. The program outputs a **priority-odered study plan** for entered subjects

# Sample Input
Number of subject:3 Subject1: Math Difficulty(1-5): 4 Deadline(days left):5
Subject2: Physics Difficulty(1-5):3 Deadline(days left):7 
Subject3: Cemistry Difficulty(1-5): 5 Deadline(days left):3

# Sample output
Collected Subjects and Priorities: Chemistry: Difficulty=5, Deadline = 3 , Estimated Study Hours =6
Math: Difficulty=5, Deadline = 3, Estimated Study Hours =5
Physics: Difficulty=3, Deadline =7, Estimated Study Hours =3

# future enhancements
- Include **Student details**: Name, College, Graduation year, Email
- Imclude **credit for each subject**
- include **daily study hours** and preferred study times
- Include **strong/weak** areas and confidence levels
- Actionable next step suggestions(eg. "Revise tree before Graphs")
- visualistaion: color-coded past schedule, calender veiw
- Adaptive logic using past performance and learning speed

## Demo instructions

-Run 'main.py' in Replit
-Input Subjects, Difficulty, and deadlines
-Observe priority-sorted output
-Record the screen (optional, for hackathon submission vedio)

## Submission Notes
- This repositry is **public**
- MVP  ready for **hackathon submission**
- can be enhanced later without breaking current logic
- Submission Link: [

