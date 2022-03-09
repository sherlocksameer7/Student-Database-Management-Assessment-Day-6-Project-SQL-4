import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("student.db")

list_of_Tables = connection.execute("Select name from sqlite_master Where type='table' And name='Student_Database'").fetchall()

if list_of_Tables != []:

    print("Table not found! ")

else:
    connection.execute(''' Create Table Student_Database(
                       ID Integer Primary Key Autoincrement,
                       Name Text,
                       Roll_Number Integer,
                       Admission_Number Integer,
                       Exam_Name Text,
                       English Integer,
                       Mathematics Integer,
                       Physics Integer,
                       Chemistry Integer,
                       Biology Integer
    ); ''')
    print("Table created successfully")

while True:
    print("Select an from the Option Menu: ? ")

    print("1. Add a Student ")
    print("2. View all Students ")
    print("3. Search a Student using Partial Name or Letter ")
    print("4. Search a Student using Roll Number or Admission Number ")
    print("5. Update a Student with Admission Number ")
    print("6. Delete a Student with Admission Number ")
    print("7. Display the Physics Topper Student Details ")
    print("8. Display the Count or Total number of the Students ")
    print("9. Display the Average marks scored in English ")
    print("10. Display the details of all Students whose score less than Average Marks in Mathematics ")
    print("11. Display the details of all Students above average students in Chemistry ")
    print("12. Exit ")

    choice = int(input("Enter a Choice ? "))

    if choice == 1:

        get_Name = input("Enter Name: ")
        get_Roll_number = input("Enter Roll Number: ")
        get_Admission_number = input("Enter Admission Number: ")
        get_Exam_name = input("Enter a Exam Name: ")
        get_English = input("Enter a English: ")
        get_Mathematics = input("Enter a Mathematics: ")
        get_Physics = input("Enter a Physics: ")
        get_Chemistry = input("Enter a Chemistry: ")
        get_Biology = input("Enter a Biology: ")

        connection.execute("Insert Into Student_Database(Name, Roll_Number, Admission_Number, Exam_Name,\
        English, Mathematics, Physics, Chemistry, Biology) Values ('"+get_Name+"', "+get_Roll_number+", "+get_Admission_number+",\
        '"+get_Exam_name+"', "+get_English+", "+get_Mathematics+", "+get_Physics+", "+get_Chemistry+", "+get_Biology+")")

        connection.commit()

        print("Inserted Successfully")

    elif choice == 2:

        result = connection.execute("Select * from Student_Database")

        table = PrettyTable(
            ["Id", "Name", "Roll Number", "Admission Number", "Exam Name", "English", "Mathematics", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

        print(table)

    elif choice == 3:

        getname = input("Enter the Partial Name to be Searched: ? ")

        result = connection.execute("Select * from Student_Database Where name like '%"+getname+"%'")

        table = PrettyTable(
            ["Id", "Name", "Roll Number", "Admission Number", "Exam Name", "English", "Mathematics", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

        print(table)

    elif choice == 4:

        get_rollnumber = input("Enter the Roll Number to be Searched: ? ")
        get_admissioNum = input("Enter the Admission Number to be Searched: ? ")

        result = connection.execute("Select * from Student_Database Where Roll_Number= "+get_rollnumber+" Or Admission_Number= "+get_admissioNum+"")

        table = PrettyTable(["Id", "Name", "Roll Number", "Admission Number", "Exam Name", "English", "Mathematics", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

        print(table)

    elif choice == 5:

        get_admission_num = input("Enter the Admission Number to be Updated: ? ")

        get_name = input("Enter the New Name: ?")
        get_rollno = input("Enter the New Roll Number: ?")
        get_exam_name = input("Enter the New Exam Name: ?")
        get_english = input("Enter the New English Mark: ?")
        get_maths = input("Enter the New Mathematics Mark: ?")
        get_physics = input("Enter the New Physics Mark: ?")
        get_chemistry = input("Enter the New Chemistry Mark: ?")
        get_biology = input("Enter the New Biology Mark: ?")

        result = connection.execute(
            "Update Student_Database Set Name= '"+get_name+"', Roll_Number= "+get_rollno+", Exam_Name= '"+get_exam_name+"',\
             English= "+get_english+", Mathematics= "+get_maths+", Physics= "+get_physics+", Chemistry= "+get_chemistry+", \
             Biology= "+get_biology+" Where Admission_Number="+get_admission_num+"")

        connection.commit()

        print("Student Data Updated Successfully")

    elif choice == 6:

        get_admino = input("Enter the Admission Number to be Deleted: ? ")

        connection.execute("Delete from Student_Database Where Admission_Number=" +get_admino)

        connection.commit()

        print(" Student Data Deleted Successfully")

    elif choice == 7:

        result = connection.execute("Select * from Student_Database Where Physics= (Select Max(Physics) from Student_Database)")

        table = PrettyTable(["Id", "Name", "Roll Number", "Admission Number", "Exam Name", "English", "Mathematics", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

        print(table)

    elif choice == 8:

        result = connection.execute("Select Count(*) as name from Student_Database")

        for i in result:

            print("Count of Student Total: ", i[0])

    elif choice == 9:

        result = connection.execute("Select Avg(English) as english from Student_Database")

        for i in result:

            print("Average Marks of English: ", i[0])

    elif choice == 10:

        result = connection.execute("Select * from Student_Database Where Mathematics < (Select Avg(Mathematics) from Student_Database)")

        table = PrettyTable(["Id", "Name", "Roll Number", "Admission Number", "Exam Name", "English", "Mathematics", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

        print(table)

    elif choice == 11:

        result = connection.execute(
            "Select * from Student_Database Where Chemistry > (Select Avg(Chemistry) from Student_Database)")

        table = PrettyTable(["Id", "Name", "Roll Number", "Admission Number", "Exam Name", "English", "Mathematics", "Physics", "Chemistry", "Biology"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])

        print(table)

    elif choice == 12:

        connection.close()

        break

    else:

        print("Invalid Choice!!! ")