# import sqlite3
#
# connect = sqlite3.connect("students.db")
# cursor = connect.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     grade TEXT
# )
# """)
#
# connect.commit()
#
#
# def create_student(name, age, grade):
#     connect = sqlite3.connect("students.db")
#     cursor = connect.cursor()
#
#     cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
#
#     connect.commit()
#     connect.close()

#create_student("олеся", 18, "11Б")
#
# def read_students():
#     connect = sqlite3.connect("students.db")
#     cursor = connect.cursor()
#
#     cursor.execute("SELECT * FROM students")
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print(row)
#
#     connect.close()

#read_students()
#
# def update_student(name, student_id):
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#
#     cursor.execute(
#         'UPDATE students SET name = ? WHERE id = ?',
#         (name, student_id)
#     )
#
#     conn.commit()
#     conn.close()
#     print("Студент обновлён!")

#update_student("Лина", 5)
#read_students()

# def delete_student(student_id):
#     conn = sqlite3.connect("students.db")
#     cursor = conn.cursor()
#
#     cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
#
#     conn.commit()
#     conn.close()
#
# delete_student(1)
#
# read_students()

import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    grade INTEGER,
    subject TEXT
)
""")
conn.commit()
conn.close()

#print("Таблица students успешно создана в базе my_database.db")


def add_student(first_name, last_name, grade, subject):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (first_name, last_name, grade, subject)
    VALUES (?, ?, ?, ?)
    """, (first_name, last_name, grade, subject))

    conn.commit()
    conn.close()
    print(" Студент добавлен!")

def get_students():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    if students:
        print("\n Список студентов:")
        for student in students:
            print(student)
    else:
        print("Нет студентов в базе.")


def update_student(student_id, new_first_name, new_last_name):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students SET first_name = ?, last_name = ?
    WHERE id = ?
    """, (new_first_name, new_last_name, student_id))

    conn.commit()
    conn.close()
    print("Данные студента обновлены!")

def delete_student(student_id):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()
    print("Студент удалён!")

add_student("Камила", "Абдукаимова", 10, "Математика")
add_student("Ислам", "Казакбаев", 11, "Литература")
add_student("Лина", "Осмонова", 9, "Физика")

get_students()

update_student(3, "Азалина", "Мусабаева")

get_students()

delete_student(3)

get_students()












