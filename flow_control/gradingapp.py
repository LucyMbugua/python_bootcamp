"""Create a console app that asks for student name, class, class teacher
Ask for the scores of Math, Eng, Kisw, Sci, SST
compute: total score and average score
using the following system grade the student based on the average score
80-100 A
75-79 A-
70-74 B+
65-69 B
60-64 B-
55-59 C+
50-54 C
45-49 C-
40-44 D+
35-39 D
30-34 D-
0-29 E
<0 or >100 Invalid
"""
# automate the gradingapp system to ensure that it uses a forloop to ask for the five subjects marks
#student details

student_name = input("Enter your name:\n")
student_class = input("Enter your class:\n")
clclass_teacher =  input("Enter your class teacher's name:\n")

#scores per subject
total_score = 0
subjects = ["math", "Eng", "Kiswahili", "Science", "Social Studies"]
for i in range(len(subjects)):
  
   marks = int(input("What is your" +" "+ subjects[i] +" "+"score:\n"))
   total_score += marks

#average score
average_score = total_score/5
print(student_name +"'s "+ "average score is"+ " ", average_score)

#if else
if average_score<=100 and average_score>79:
    print("Grade A")
elif average_score<80 and average_score>74:
    print("Grade A-")
elif average_score<75 and average_score>69:
    print("Grade B+")
elif average_score<70 and average_score>64:
    print("Grade B")
elif average_score<65 and average_score>59:
    print("Grade B-")
elif average_score<60 and average_score>54:
    print("Grade C+")
elif average_score<55 and average_score>49:
    print("Grade C")
elif average_score<50 and average_score>44:
    print("Grade C-")
elif average_score<45 and average_score>39:
    print("Grade D+")
elif average_score<40 and average_score>34:
    print("Grade D")
elif average_score<35 and average_score>29:
    print("Grade D-")
else:
    print("Grade Invalid")

    
    

