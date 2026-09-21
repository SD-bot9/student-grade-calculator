class StudentRecord:
    def __init__(self, student_name):
        self.student_name = student_name
        self.marks = {}  # Format: {'Subject Name': marks_obtained}

    def add_marks(self, subject_name, score):
        if subject_name in self.marks:
            print(f"Warning: Overwriting previous marks for {subject_name}.")
        self.marks[subject_name] = score
        print(f"Added {subject_name}: {score}")
