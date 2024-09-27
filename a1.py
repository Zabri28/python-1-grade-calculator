lab = int(input("Enter the number of labs completed"))
if lab > 6:
	lab = 6
lab_score = (lab / 6) * 100 * 0.2
quiz = int(input("Enter the number of quizzes completed"))
if quiz > 6:
	 quiz = 6
quiz_score = (quiz / 6) * 100 * 0.15
assignment1 = int(input("Enter grade for Assignment 1"))
assignment1_score = (assignment1 * 0.04)
assignment2 = int(input("Enter grade for Assignment 2"))
assignment2_score = (assignment2 * 0.04)
assignment3 = int(input("Enter grade for Assignment 3"))
assignment3_score = (assignment3 * 0.04)
assignment4 = int(input("Enter grade for Assignment 4"))
assignment4_score = (assignment4 * 0.04)
midterm1 = int(input("Enter grade for Midterm 1"))
midterm1_score = (midterm1 * 0.125)
midterm2 = int(input("Enter grade for Midterm 2"))
midterm2_score = (midterm2 * 0.125)
exam = int(input("Enter grade for Final Exam"))
exam_score = (exam * 0.18)
midfin = int(input("Enter grade for Midterms and Final Preparation"))
midfin_score = (midfin * 0.06)
x = lab_score + quiz_score + assignment1_score + assignment2_score + assignment3_score + assignment4_score + midterm1_score + midterm2_score + exam_score + midfin_score
print ("Your grade is", (x))
