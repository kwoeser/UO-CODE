# Import routines
import os
from cis122_assign06_shared_correct import pad_left, pad_right

while True:
   filename = input("Enter filename (blank to exit): ")
   if len(filename.strip()) == 0:
      break
   elif not os.path.exists(filename):
      print("Invalid filename:",filename)
   else:
      fin = open(filename)
      count = 0
      comments = 0
      total = 0
      for line in fin:
         num = line.strip()
         first = num[0]
         if len(num) > 0 and first != '#':
            count = count + 1
            total = total + int(num)
         else:
            comments = comments + 1

      # Close file
      fin.close()

      label_spacing = 10
      num_spacing = 10
      print(pad_right("Count:", label_spacing), pad_left(count, num_spacing))
      print(pad_right("Comments:", label_spacing), pad_left(comments, num_spacing))
      print(pad_right("Total:", label_spacing), pad_left(total, num_spacing))
      print(pad_right("Average:", label_spacing), pad_left(round(total/count,2), num_spacing))
