student_heights = input("Please introduce a list of student heights.").split()

for n in range (0, len(student_heights)):
	student_heights[n] = int(student_heights[n]) # we need to convert our imputs str to int...


result = 0 
a = 0 
for height in student_heights: # we make a sum of each one of the heights 
	result += height
	a += 1 

print(f" The averange height is: {round(result/a)}")