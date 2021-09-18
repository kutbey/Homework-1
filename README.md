# Homework-1
Parsing the data from the data.txt file and writing it to other files as desired 
This is a sample data parsing exercise
Generally
The data is taken from the data.txt file. The data were written to other files according to the grades of the students.

# Base data format
Eleanor-Taylor Fizik 78/90/70
Lyla-Dawson Matematik 98/67/100
Cora-Gill-Maryam Matematik Müh 76/78/93

# Desired format(this is how it will be written to other files)
| Name          | Surname   | Department     | E1   | E2   | Fin  | Average | Letter | Status |
| ------------- | --------- | -------------- | ---- | ---- | ---- | ------- | ------ | ------ |
| Robin         | Spencer   | Matematik      | 89   | 98   | 97   | 94.90   | AA     | Passed |
| Marley Sienna | Robertson | Bilgisayar Müh | 99   | 100  | 69   | 87.30   | FF     | Failed |

# avarage note calculation
:param ex1: midterm 1
:param ex2: midterm 1
:param fin: final exam
midterm_rate=30 , final_rate=40
avarageNoteFormul = ((ex1 + ex2) * midterm_rate) + (fin * final_rate)

# Student's passing conditions
passing grade=60 final grade=70
avarage note > passing grade and final exam > final grade



# Letter Note(Optional)
letterNote()  and isPassed() view its functions 