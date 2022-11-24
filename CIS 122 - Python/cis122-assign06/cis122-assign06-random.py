# CIS 122 Fall 2021 Assignemnt 6 
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: random problem


# Never ended up using pad_right so I only imported pad_left
from cis122_assign06_shared import pad_left
import os

count = 0
comments = 0
total = 0
label_spacing = ' '
num_spacing = 10


while True:
    file = input('Enter filename (blank to exit): ')
    file = file.strip() # Strips away the white space

    if len(file) == 0:  # When nothing is inputted it closes the file and ends loops
        break

    # If inputted filename doesn't exist then it will say it's invalid but the loop will countiue
    elif not os.path.exists(file):
        print('Invalid filename: ' + file)

    # If the inputted filename exists then it will open the file
    elif os.path.exists(file):
        open_file = open(file) # Opens the file
            
        for line in open_file: 
            if '#' in line: # Looks for every # in the file
                comments += 1

            elif '#' not in line: # Looks for anything that does start with # in the file
                count += 1
                # adds each line to total until for loop is finished
                total += int(line)
 

        open_file.close() # Closes the file

        
        avg = total / count # Finds average of the total numbers
        # Calls the pad_left function from the shared python file and gives the function
        # it's arguments. It makes a padding to the left of the output. Kinda like an HTML effect
        print('Count:', pad_left(count,num_spacing + 8, label_spacing))
        print('Comments:', pad_left(comments,num_spacing + 4, label_spacing))
        print('Total:', pad_left(total,num_spacing + 8, label_spacing))
        print('Average:', pad_left(round(avg, 2),num_spacing + 2, label_spacing))

                
    
    





