from tkinter import *
from tkinter import messagebox
from database import Database

database = Database("attendance.db")

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Attendance Management System")
        self.master.geometry("800x500")

        self.student_name = StringVar()
        self.student_class = StringVar()
        self.teacher_name = StringVar()
        self.class_name = StringVar()
        self.date = String
# ...

        self.present = BooleanVar()
        self.activity = StringVar()

        # create labels
        self.lbl_title = Label(self.master, text="Attendance Management System", font=("Arial", 24))
        self.lbl_title.pack(pady=10)

        self.lbl_student = Label(self.master, text="Student Details", font=("Arial", 16))
        self.lbl_student.pack(pady=5)

        self.lbl_name = Label(self.master, text="Name:", font=("Arial", 12))
        self.lbl_name.pack()

        self.lbl_class = Label(self.master, text="Class:", font=("Arial", 12))
        self.lbl_class.pack()

        self.lbl_teacher = Label(self.master, text="Teacher Details", font=("Arial", 16))
        self.lbl_teacher.pack(pady=5)

        self.lbl_tname = Label(self.master, text="Name:", font=("Arial", 12))
        self.lbl_tname.pack()

        self.lbl_classname = Label(self.master, text="Class Name:", font=("Arial", 12))
        self.lbl_classname.pack()

        self.lbl_attendance = Label(self.master, text="Attendance Details", font=("Arial", 16))
        self.lbl_attendance.pack(pady=5)

        self.lbl_date = Label(self.master, text="Date:", font=("Arial", 12))
        self.lbl_date.pack()

        self.lbl_present = Label(self.master, text="Present:", font=("Arial", 12))
        self.lbl_present.pack()

        self.lbl_activity = Label(self.master, text="Activity:", font=("Arial", 12))
        self.lbl_activity.pack()

        # create entry boxes
        self.ent_name = Entry(self.master, textvariable=self.student_name, font=("Arial", 12))
        self.ent_name.pack()

        self.ent_class = Entry(self.master, textvariable=self.student_class, font=("Arial", 12))
        self.ent_class.pack()

        self.ent_tname = Entry(self.master, textvariable=self.teacher_name, font=("Arial", 12))
        self.ent_tname.pack()

        self.ent_classname = Entry(self.master, textvariable=self.class_name, font=("Arial", 12))
        self.ent_classname.pack()

        self.ent_date = Entry(self.master, textvariable=self.date, font=("Arial", 12))
        self.ent_date.pack()

        self.chk_present = Checkbutton(self.master, variable=self.present, font=("Arial", 12))
        self.chk_present.pack()

        self.ent_activity = Entry(self.master, textvariable=self.activity, font=("Arial", 12))
        self.ent_activity.pack()

        # create buttons
        self.btn_add_student = Button(self.master, text="Add Student", command=self.add_student)
        self.btn_add_student.pack(pady=10)

        self.btn_add_teacher = Button(self.master, text="Add Teacher", command=self.add_teacher)
        self.btn_add_teacher.pack(pady=10)

        self.btn_add_class = Button(self.master, text="Add Class", command=self.add_class)
        self.btn_add_class.pack(pady=10)

        self.btn_mark_attendance = Button(self.master, text="Mark Attendance", command=self.mark_attendance)
        self.btn_mark_attendance.pack(pady=10)

        # create listboxes
        self.lb_students = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_students.pack(side=LEFT, padx=20, pady=20)

        self.lb_teachers = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_teachers.pack(side=LEFT, padx=20, pady=20)
# ...

        # create listboxes
        self.lb_students = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_students.pack(side=LEFT, padx=20, pady=20)

        self.lb_teachers = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_teachers.pack(side=LEFT, padx=20, pady=20)

        self.lb_classes = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_classes.pack(side=LEFT, padx=20, pady=20)

        self.lb_attendance = Listbox(self.master, width=70, font=("Arial", 12))
        self.lb_attendance.pack(side=LEFT, padx=20, pady=20)

        # create scrollbar for attendance listbox
        self.attendance_scrollbar = Scrollbar(self.master)
        self.attendance_scrollbar.pack(side=LEFT, fill=Y)

        # set the scrollbar to the attendance listbox
        self.lb_attendance.config(yscrollcommand=self.attendance_scrollbar.set)
        self.attendance_scrollbar.config(command=self.lb_attendance.yview)

    def add_student(self):
        """Add a new student to the listbox"""

        name = self.student_name.get()
        std_class = self.student_class.get()

        if name and std_class:
            self.school.add_student(name, std_class)
            self.update_student_listbox()

    def add_teacher(self):
        """Add a new teacher to the listbox"""

        name = self.teacher_name.get()
        cls_name = self.class_name.get()

        if name and cls_name:
            self.school.add_teacher(name, cls_name)
            self.update_teacher_listbox()

    def add_class(self):
        """Add a new class to the listbox"""

        cls_name = self.class_name.get()

        if cls_name:
            self.school.add_class(cls_name)
            self.update_class_listbox()

    def mark_attendance(self):
        """Mark attendance for a student in a particular class on a particular date"""

        name = self.student_name.get()
        std_class = self.student_class.get()
        teacher = self.teacher_name.get()
        cls_name = self.class_name.get()
        date = self.date.get()
        present = self.present.get()
        activity = self.activity.get()

        if name and std_class and teacher and cls_name and date:
            self.school.mark_attendance(name, std_class, teacher, cls_name, date, present, activity)
            self.update_attendance_listbox()

    def update_student_listbox(self):
        """Update the student listbox with the current students in the school"""

        self.lb_students.delete(0, END)

        for student in self.school.students:
            self.lb_students.insert(END, student)

    def update_teacher_listbox(self):
        """Update the teacher listbox with the current teachers in the school"""

        self.lb_teachers.delete(0, END)

        for teacher in self.school.teachers:
            self.lb_teachers.insert(END, teacher)

    def update_class_listbox(self):
        """Update the class listbox with the current classes in the school"""

        self.lb_classes.delete(0, END)

        for cls in self.school.classes:
            self.lb_classes.insert(END, cls)

    def update_attendance_listbox(self):
        """Update the attendance listbox with the current attendance records"""

        self.lb_attendance.delete(0, END)

        for record in self.school.attendance_records:
            self.lb_attendance.insert(END, record)

    def run(self):
        """Run the application"""

        self.master.mainloop()

    if 

class Interface:
    """The graphical user interface for the attendance tracker"""

    def __init__(self, master):
        """Initialize the interface"""

        self.master = master
        self.master.title("Attendance Tracker")

        # create school instance
        self.school = School()

        # create labels
        self.student_label = Label(self.master, text="Student Name:")
        self.student_label.pack(side=TOP, pady=10)

        self.teacher_label = Label(self.master, text="Teacher Name:")
        self.teacher_label.pack(side=TOP, pady=10)

        self.class_label = Label(self.master, text="Class Name:")
        self.class_label.pack(side=TOP, pady=10)

        self.date_label = Label(self.master, text="Date (YYYY-MM-DD):")
        self.date_label.pack(side=TOP, pady=10)

        self.present_label = Label(self.master, text="Present:")
        self.present_label.pack(side=TOP, pady=10)

        self.activity_label = Label(self.master, text="Activity:")
        self.activity_label.pack(side=TOP, pady=10)

        # create entry fields
        self.student_name = Entry(self.master, width=30, font=("Arial", 12))
        self.student_name.pack(side=TOP, padx=20, pady=5)

        self.teacher_name = Entry(self.master, width=30, font=("Arial", 12))
        self.teacher_name.pack(side=TOP, padx=20, pady=5)

        self.class_name = Entry(self.master, width=30, font=("Arial", 12))
        self.class_name.pack(side=TOP, padx=20, pady=5)

        self.date = Entry(self.master, width=30, font=("Arial", 12))
        self.date.pack(side=TOP, padx=20, pady=5)

        self.present = BooleanVar()
        self.present_checkbox = Checkbutton(self.master, variable=self.present)
        self.present_checkbox.pack(side=TOP, padx=20, pady=5)

        self.activity = Entry(self.master, width=30, font=("Arial", 12))
        self.activity.pack(side=TOP, padx=20, pady=5)

        # create buttons
        self.add_student_button = Button(self.master, text="Add Student", command=self.add_student)
        self.add_student_button.pack(side=LEFT, padx=20, pady=20)

        self.add_teacher_button = Button(self.master, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack(side=LEFT, padx=20, pady=20)

        self.add_class_button = Button(self.master, text="Add Class", command=self.add_class)
        self.add_class_button.pack(side=LEFT, padx=20, pady=20)

        self.mark_attendance_button = Button(self.master, text="Mark Attendance", command=self.mark_attendance)
        self.mark_attendance_button.pack(side=LEFT, padx=20, pady=20)

        # create listboxes
        self.lb_students = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_students.pack(side=LEFT, padx=20, pady=20)

        self.lb_teachers = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_teachers.pack(side=LEFT, padx=20, pady=20)

        self.lb_classes = Listbox(self.master, width=30, font=("Arial", 12))
        self.lb_classes.pack(side=LEFT, padx=20, pady=20)

        self.lb_attendance = Listbox(self.master, width=70, font=("Arial", 12))
