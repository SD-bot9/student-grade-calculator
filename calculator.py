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

