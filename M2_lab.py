'''
Program: Dean's list / honor roll checker
Version: 1.0
Date: 1 September 2024
Author: Erin Hurm
Purpose: Accepts a student's first and last name, checks whether their GPA is high enough for them to be on the Honor Roll or Dean's List.
'''

#variables
lastName = ""
firstName = ""
studentGPA = 0

#constants || dl = dean's list, hr = honor roll
dlGPA = 3.5
hrGPA = 3.25

lastName = input("Enter the student's last name (or ZZZ to exit): ")

while not lastName == "ZZZ":
    firstName = input("Enter the student's first name: ")
    studentGPA = float(input("Enter the student's GPA: "))
    
    if studentGPA >= dlGPA:
        print(f"{firstName} {lastName} has made the Dean's List!")
    elif studentGPA >= hrGPA:
        print(f"{firstName} {lastName} has made the Honor Roll!")

    lastName = input("Enter the student's last name (or ZZZ to exit): ")

print("End program.")