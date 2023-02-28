import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, class TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS classes (id INTEGER PRIMARY KEY, name TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS attendance (id INTEGER PRIMARY KEY, student_id INTEGER, date TEXT, present INTEGER, activity TEXT)")
        self.conn.commit()

    def insert_student(self, name, class):
        self.cur.execute("INSERT INTO students VALUES (NULL, ?, ?)", (name, class))
        self.conn.commit()

    def fetch_students(self, class):
        self.cur.execute("SELECT * FROM students WHERE class=?", (class,))
        rows = self.cur.fetchall()
        return rows

    def insert_teacher(self, name):
        self.cur.execute("INSERT INTO teachers VALUES (NULL, ?)", (name,))
        self.conn.commit()

    def fetch_teachers(self):
        self.cur.execute("SELECT * FROM teachers")
        rows = self.cur.fetchall()
        return rows

    def insert_class(self, name):
        self.cur.execute("INSERT INTO classes VALUES (NULL, ?)", (name,))
        self.conn.commit()

    def fetch_classes(self):
        self.cur.execute("SELECT * FROM classes")
        rows = self.cur.fetchall()
        return rows

    def mark_attendance(self, student_id, date, present, activity):
        self.cur.execute("INSERT INTO attendance VALUES (NULL, ?, ?, ?, ?)", (student_id, date, present, activity))
        self.conn.commit()

    def fetch_attendance(self, student_id):
        self.cur.execute("SELECT * FROM attendance WHERE student_id=?", (student_id,))
        rows = self.cur.fetchall()
        return rows

    def delete_student(self, id):
        self.cur.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()

    def delete_teacher(self, id):
        self.cur.execute("DELETE FROM teachers WHERE id=?", (id,))
        self.conn.commit()

    def delete_class(self, id):
        self.cur.execute("DELETE FROM classes WHERE id=?", (id,))
        self.conn.commit()

    def update_class(self, id, class):
        self.cur.execute("UPDATE students SET class=? WHERE id=?", (class, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
