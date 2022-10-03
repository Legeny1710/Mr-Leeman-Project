import time



#Title
print("WELCOME TO STUDENT DATA BASE!")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")

#Login
def login():
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")  
  for line in open("UN&PA.txt","r").readlines():
    login_info = line.split()
    while username != login_info[0] and password != login_info[1]:
      print("Incorrect.")
      if username != login_info[0]:
        username = input("Please enter your username: ")
      elif password != login_info[1]:
        password = input("Please enter your password: ")    
    else:
      print("Correct!")

#login()

#MENU
print("Menu:")
time.sleep(0.5)
print("1. Enter student details")
time.sleep(0.5)
print("2.Display the details of students")
time.sleep(0.5)
print("3.Enter student's grades")
time.sleep(0.5)
print("4.Log out")

#mc = Menu Choice
mc = int(input("What do you wanna do?... (Pick a number): "))

def esd(a):
  while True:
    if a == 1:
      print("You are on 'Enter Student details' ")
      print("")
      ID = input("Enter ID: (must be 8 digits or more!): ")
      while len(str(ID)) < 8:
        print("MUST BE 8 DIGITS OR MORE!")
        print("Your password", len(str(ID)), "digits")
        ID=input("Try again!, Enter ID: ")
      if len(str(ID)) > 8:
        print("")
      time.sleep(0.4)

      Forname=input("Enter Forename: ")
      time.sleep(0.4)

      surname=input("enter Surname: ")
      time.sleep(0.4)

      print("Enter the date of birth ")
      day=input("Day: ")
      time.sleep(0.4)
      month=input("Month: ")
      time.sleep(0.4)
      year=input("Year: ")

      homeadress=input("Enter the home adress: ")
      time.sleep(0.4)

      homephonenumber=input("enter the home phone number: ")
      time.sleep(0.4)

      gender=input("Enter the gender: ")
      while gender != "Female" and gender != "Male":
         gender=input("Try again!, Enter the gender: ")
      else:
        print("")
      
      time.sleep(0.4)

      Tutorgroup=input("Enter tutor group: ")
      time.sleep(0.5)
      
      schoolgmailadress=input("Enter the school email adress: (Do not include 'qmschool.org.uk')")

      file=open("StudentDetails.txt", "a")
      file.write("|"+"ID: "+ID+"|"+"Forname:"+Forname+" |"+"Surname: "+surname+" |"+"Date of Birthday: "+day+"/"+month+"/"+year+" |"+"Home adress: "+homeadress+" |"+"Home Phone number: "+homephonenumber+" |"+"Gender: "+gender+" |"+"Tutor group: "+Tutorgroup+" |"+"School gmail Adress: "+ schoolgmailadress+"@qmschool.org.uk"+"|"+"\n\n")
      file.close()

      print("Student has added!")

      a = int(input("What do you wanna do?... (Pick a number): "))

    elif a == 2:
      print("You are on 'Display the details of students' ")
      print("If you want to see all students say 'all' or type 'ID' to search student by their ID or name:")
      d = input("=: ")
      if d == "all":
        print("Here are the all Students")
        time.sleep(0.4)
        file=open("StudentDetails.txt", "r")
        lines=file.readlines()
        for line in lines:
          print(line)
          file.close() 
      elif d == "ID":
        id = input("Search ID: ")
        file=open("StudentDetails.txt", "r")
        lines = file.readlines()
        new_list = []
        idx = 0
        for line in lines:
            if id in line:
                new_list.insert(idx, line)
                idx += 1
        file.close()
        if len(new_list)==0:
            print("Couldn't find ID!")
        else:
            lineLen = len(new_list)
            for i in range(lineLen):
                print(end=new_list[i])
            print()
        
      a = int(input("What do you wanna do?... (Pick a number): "))
    elif a == 3:
      student = str(input("Enter student name: ")) 
      split_line=open("StudentDetails.txt")
      split_line = split_line.readline()
      if len(split_line) == 0:
        print("no line")
        split_line.close()
      elif len(split_line) > 0:
        if student in split_line:
          file1=open("StudentDetails.txt")
          file1.write("lets go")
          print("Grade added")
      a = int(input("What do you wanna do?... (Pick a number): "))
    elif a == 4:
      time.sleep(0.2)
      print(".")
      time.sleep(0.3)
      print("..")
      time.sleep(0.3)
      print("...")
      time.sleep(0.3)
      print("You logged out!")
      break
    else:
      print("That's not correct number!")
      a = int(input("What do you wanna do?... (Pick a number): "))

esd(mc)
