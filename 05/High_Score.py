student_scores = input("Please introduce a list of scores").split()

for n in range(0,len(student_scores)):
	student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0
for n in student_scores:
	if n > highest:
		highest = n 

print(f"The highest scores is: {highest}")