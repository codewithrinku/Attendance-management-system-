# 🎓 Student Attendance Management System (Python + sql)
### This project is database student attendece project
import sqlite3 as sql
from datetime import datetime
data = sql.connect(database = "Attendence.db")
cursor = data.cursor()
cursor.execute("""create table IF NOT EXISTS student (
               Date TEXT,
               Name TEXT,
               class TEXT,
               roll_number INT,
               Status TEXT)""")
data.commit()
data.close()

while True:
    try:
        print("\t================ATTENDENCE MANAGEMENT SYSTEM===============\n\n")
        print("1. Mark Attendence")
        print("2. View Attendence")
        print("3. Delete All Attendance Data")
        print("4. Exit ")
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("❌Invalid number")
        continue
   
    if (choice == 1):
        data_list = []
        try:
            number = int(input("\nEnter how many student data store in database : "))
        except ValueError:
            print("❌Invalid number")
        for i in range(1,number+1):
            date = datetime.now().strftime("%d-%m-%Y")
            name = input(f"Enter {i} Name : ")
            clas = input("Enter class : ")
            try:
                roll_number = int(input("Enter roll number : "))
            except ValueError:
                print("❌Invalid number check your number ")
                continue
            status = input("Enter Attendence : ")
            data_list.append((date,name,clas,roll_number,status))
                

        data = sql.connect("Attendence.db")
        cursor = data.cursor()
        cursor.executemany("""insert into student (
               Date ,
               Name ,
               class ,
               roll_number ,
               Status ) values (?,?,?,?,?)""",data_list)
        data.commit()
        data.close()
        print("🏆Data saved successfully")
    elif (choice == 2):
        data = sql.connect("Attendence.db")
        cursor = data.cursor()
        cursor.execute("select * from student")
        fetch_data = cursor.fetchall()
        print("\t\t=======student record==========\n")
        print("DATE | NAME | CLASS | ROLL | STATUS\n")
        for data in fetch_data:
            print(" | ".join(map(str, data)))
    elif choice == 3:
        confirm = input(" Are you sure you want to delete all attendance records? (yes/no): ").lower()
        if confirm == 'yes':
            data = sql.connect("Attendence.db")
            cursor = data.cursor()
            cursor.execute("Delete from student")
            data.commit()
            data.close()
            print(" ❌ All data deleted successfully.")
        else:
            print("❌ Deleted cancelled.")

    elif (choice == 4):
        print("🙏Thanku for using my database🙏")
        break
    else:
        print("❌ Invalid choice! Please choose 1, 2 or 3.")
