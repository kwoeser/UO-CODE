# CIS 122 Fall 2021 Lab 6
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: Grades problem

count = 0
total = 0
input_grades = True
lowest_grade = 101
highest_grade = -1

while input_grades:
    grade = input("Enter score (blank to quit): ")

    if len(grade) == 0:
        input_grades = False

    # If the input is anything but 0 it will do the following; turns grade into a int and adds 1 to
    # count. Also adds real_grade to the total. This all happens until the loop is finished.
    else:
        real_grade = int(grade)
        count += 1
        total += real_grade

        # Whichever input is more less then 101 will become the lowest_grade
        if real_grade < lowest_grade:
            lowest_grade = real_grade

        # Whichever input is more more then -1 will become the highest_grade
        elif real_grade > highest_grade:
            highest_grade = real_grade

# If the count is more then 0 it will print the results
if count  > 0:
    avg = round(total/count)
    print("*** Results ***")
    print("Count:", count)
    print("Average:", avg)
    print("Low Score:", lowest_grade)
    print("Highest Score:", highest_grade)

else:
    print("No Score's were entered")
