# Smart Adaptive Study Planner

## Project Description
This is a **Smart Adaptive Study Planner** designed for students to help them plan their study schedule **intelligently**. It prioritizes subjects based on **difficulty** and **upcoming deadlines**, while also considering cognitive load to prevent burnout.  

The planner is **adaptive**, meaning it adjusts priorities and estimated study hours based on user inputs for **difficulty**, **deadline**, and **available study hours**. It provides a **clear, actionable daily plan**.

---

## Features

- **Priority Calculation:** Priority = Difficulty / Deadline  
- **Emergency Boost:** If a subject’s exam is near (≤ 2 days), its priority is increased  
- **Cognitive Load Adjustment:** Reduces study hours for very difficult subjects to prevent burnout  
- **Sorted Study Plan:** Subjects are listed from highest to lowest priority  
- **Adaptive & Transparent:** Students can understand why a subject has higher priority  

---

## How to Use

1. Run `main.py`
2. Enter **student details**: Name, Graduation Year, Email  
3. Enter **available study hours** for weekdays and weekends  
4. Enter **number of subjects**  
5. For each subject, enter:
   - Subject name  
   - Difficulty (1-5)  
   - Deadline (days left)  
6. The program generates:
   - Collected subjects and deadlines  
   - Estimated study hours per subject  
   - Smart, prioritized study plan  

---

## Sample Input
Name: Aman Graduation Year: 2026 Email: aman@example.com Weekday hours: 3 Weekend hours: 6 Subjects: Data Structures, Operating Systems, Engineering Mathematics Difficulties: 4, 5, 3 Deadlines (days left): 3, 2, 5


## Sample Output
Collected Subjects and Deadlines: Data Structures: Difficulty=4, Deadline=3 Operating Systems: Difficulty=5, Deadline=2 Engineering Mathematics: Difficulty=3, Deadline=5
Generating Your Smart Plan: Subject          Difficulty Deadline  Est. Hours Operating Systems 5         2         6.5 Data Structures   4         3         5.0 Engineering Mathematics 3   5         3.5
Plan for: Aman, Graduation Year: 2026, Email: aman@example.com

## Future Goals / Extensions

- Include **strong/weak areas** per subject to personalize priorities  
- Track **student performance & learning speed** to adapt study plans dynamically  
- Include **peer-to-peer learning** suggestions  
- Add a **graphical interface** with a visual calendar view  
- Integrate AI/ML to predict **optimal learning sequence** for each student  



## Hackathon Notes

- This project is a **working MVP** for the hackathon submission  
- It demonstrates **impactful, practical, and personalized study planning**  
- GitHub repo contains **main.py** and this README for reference
