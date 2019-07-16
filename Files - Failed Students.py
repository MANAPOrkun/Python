students_numb = int(input("Enter number of students: "))

def AddStudentDatabase(students_numb):



    students_database = []

    for i in range(students_numb):

        students_name = input("Enter students name: ")
        students_id = input("Enter students id: ")
        students_mark = input("Enter students alphabet mark: ")

        students_database.append([str(i+1),students_name,students_id,students_mark])

    return students_database

def SaveToFile(Student_List):

    with open("Student Database.txt","w",encoding="utf-8") as students_file:

        students_file.write("   Name\t\tID\tMark\n")

        for student in Student_List:

            for info in student:

                if(info == student[0]):

                    students_file.write(info+") ")
                    student[0] = 0

                else:

                    students_file.write(info+" \t")

            students_file.write("\n")

def Failed_Students(Student_List):

    with open("Failed Students.txt","w",encoding="utf-8") as failed:

        failed.write("   Name\t\tID\tMark\n")

        count = 1

        for student in Student_List:

            if(student[3] == "FF"):

                for info in student:

                    if (info == student[0]):

                        failed.write(str(count) + ") ")
                        count+=1

                    else:

                        failed.write(info + " \t")

                failed.write("\n")


Student_List = AddStudentDatabase(students_numb)

SaveToFile(Student_List)

Failed_Students(Student_List)



