# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:09:30 2021

@author: user
"""
class StudentGrader:
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        
    def calculate_final_mark(self):
        return self.mark1 * 0.2 + self.mark2 * 0.4 + self.mark3 * 0.4
    
    def get_grade(self):
        all_marks = self.calculate_final_mark()
        
        if(0<=all_marks<=44):
            if(self.mark1 == 0 or self.mark2 == 0):
                grade = 'AF'
            else:
                grade = 'F'
        elif(49>= all_marks >=45):
            if(self.mark1 <50):
                if(self.mark1 == 0 or self.mark2 == 0 or self.mark3 ==0):
                    if(0< self.mark2 <50):
                        grade = "SA"
                else:
                    grade = "F"
            elif(0> self.mark2 < 50):
                if(self.mark1 == 0 or self.mark2 == 0 or self.mark3 == 0):
                    if((0< self.mark1 <50) or self.mark2 <50):
                        grade = 'SA'
                else:
                    grade = 'F'
            else:
                grade = 'SE'
        elif(64 >= all_marks >= 50):
            grade = 'P'
        elif(74 >= all_marks >= 65):
            grade = 'C'
            # final mark is between 75 - 84 (inclusive)
        elif(84 >= all_marks >= 75 ):
            grade = 'D'
        # final mark is between 85 - 100 (inclusive)
        elif(100>= all_marks >= 85):
            grade = 'HD'            
        return grade
    
#three_input = list(map(float, input('Enter a student\'s assessment marks (separated by comma): ')
                  #.split(',')))
#class StudentGrade accepts multiple kwargs or marks1, marks2, marks3
#print(StudentGrader(*three_input).get_grade())

while True:
    print("Choose one of the following options: ")
    print("1 - Enter student grade information")
    print("2 - Print all student grade information")
    print("3 - Print class performance statistics")
    print("4 - Exit")
    
    main_choices = input()
    
    if(main_choices == "1"):
        while True:
            
            
            print("Choose one of the following options: ")
            print("1.1 - Enter a BIT student information")
            print("1.2 - Enter a DIT student information")
            print("1.3 - Go back to the main menu")
            
            choice_opts = input()
            if(choice_opts=="1.1"):
        
                #student details include ID, name, and *three_input asterixs represents all the three marks inputed
                stud_idn = input("Enter student ID: ")
                stud_nme = input("Enter student name: ")
                three_input = list(map(float, input('Enter a student\'s assessment marks (separated by comma): ')
                                  .split(',')))
                
                #calculate the grade using the get grade method defined in the class
                grade_letter = StudentGrader(*three_input).get_grade()
                
                #check for assessment or exam retake incase the grade is an SA, or SE
                if grade_letter == "SE":

                    # get new supplementary exam mark from user
                    sup_exam_input = input("What is this student's supplementary examm mark: ")

                elif grade_letter == "SA":

                    # get new supplementary assessment marks from user
                    sup_marks = input("What is this student's supplementary assessment mark: ")
            
            #choice_opts = input()
            
            elif(choice_opts=="1.2"):
                
                #student details include ID, name, and *three_input asterixs represents all the three marks inputed
                stud_idn = input("Enter student ID: ")
                stud_nme = input("Enter student name: ")
                three_input = list(map(float, input('Enter a student\'s assessment marks (separated by comma): ')
                                  .split(',')))
                
                #calculate the marks using the get grade method defined in the class                
                grade_mark = StudentGrader(*three_input).calculate_final_mark()
                
                #grade marks less than 50 are resubmitted                
                if grade_mark< 50:
                    # get new resubmitted exam marks from user
                   resub_marks = list(map(float, input("What is this student's resubmission marks (separated by comma): ").split(',')))
            
            elif(choice_opts=="1.3"):
                #print("Choose only the valid options: ")
                break
                #choices = input()
            
            else:
                print("Choose one of the following options: ")
                print("1.1 - Enter a BIT student information")
                print("1.2 - Enter a DIT student information")
                print("1.3 - Go back to the main menu")
                choice_opts = input()
                
    elif(main_choices == "2"):
        print()
        #displays a student's information
        print("---------Student information-------------- ")
        listof_students = []
        i = ''
        
        if i in listof_students:
            pass
        else:
            #This is a basic student information, any student information is entered into the listof_students
            #unique record is stored in a list
            place = set([stud_idn, stud_nme])
            listof_students.append(place)
        print(listof_students)
        
            
    elif(main_choices == "3"):
        break
        #print the grading information 
        
    elif(main_choices == "4"):
        #print empty line if the information is unavailable
        #raise an exception displaying 'No information to print'
        break
                    
print(StudentGrader(*three_input).get_grade())
