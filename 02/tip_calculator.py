
print("This program is going to calculate your total account plus your tip")
total_bill = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? 10,12 or 15? ")
people_to_split = input("How many people to split the bill? ")

total_bill = float(total_bill)
percentage = float(percentage)
people_to_split = float(people_to_split)

total = (total_bill + (total_bill * percentage *.01))/people_to_split
total_r = round(total,2)
total_r = "{:.2f}".format(total_r)
print (f"Each person should pay: {total_r}")
