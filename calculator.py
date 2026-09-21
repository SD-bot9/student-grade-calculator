class StudentRecord:
    def __init__(self, student_name):
        self.student_name = student_name
        self.marks = {}  # Format: {'Subject Name': marks_obtained}

    def add_marks(self, subject_name, score):
        if subject_name in self.marks:
            print(f"Warning: Overwriting previous marks for {subject_name}.")
        self.marks[subject_name] = score
        print(f"Added {subject_name}: {score}")

 

    def calculate_percentage(self):
        if not self.marks:
            return 0.0
        total_obtained = sum(self.marks.values())
        total_possible = len(self.marks) * 100
        return (total_obtained / total_possible) * 100

    def determine_grade_and_status(self, percentage):
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        else:
            grade = 'F'
        
        # Check if failed any individual subject (marks < 40) or overall percentage < 40
        failed_subject = any(score < 40 for score in self.marks.values())
        status = "Fail" if (percentage < 40 or failed_subject) else "Pass"
        
        return grade, status


    def print_report_card(self):
        print("\n========================================")
        print(f"       REPORT CARD: {self.student_name.upper()}       ")
        print("========================================")
        if not self.marks:
            print("No subject data available.")
            return

        for sub, score in self.marks.items():
            print(f" * {sub.ljust(15)} : {score}/100")
            
        print("----------------------------------------")
        pct = self.calculate_percentage()
        grade, status = self.determine_grade_and_status(pct)
        
        print(f"Overall Percentage : {pct:.2f}%")
        print(f"Final Assigned Grade: {grade}")
        print(f"Academic Status    : {status}")
        print("========================================\n")

def main():
    print("--- Welcome to the Student Grade Calculator ---")
    name = input("Enter student name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter student name: ").strip()
        
    student = StudentRecord(name)
    
    while True:
        print("1. Add Subject Marks\n2. Generate Final Report Card\n3. Exit")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            sub_name = input("Enter subject name: ").strip()
            if not sub_name:
                print("Error: Subject name cannot be blank.\n")
                continue
            
            try:
                score_str = input(f"Enter marks for {sub_name} (0-100): ").strip()
                score = float(score_str)
                if score < 0 or score > 100:
                    print("Validation Error: Marks must remain within the 0 to 100 range.\n")
                    continue
                student.add_marks(sub_name, score)
            except ValueError:
                print("Validation Error: Numeric numerical values only.\n")
                
        elif choice == '2':
            student.print_report_card()
            
        elif choice == '3':
            print("System closed successfully.")
            break
        else:
            print("Invalid Selection! Input numbers 1 through 3 only.\n")

if __name__ == "__main__":
    main()


