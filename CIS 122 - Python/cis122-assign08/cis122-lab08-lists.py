# CIS 122 Fall 2021 Lab 8
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: lists lab

import random

def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
   '''Purpose: Genereates a random number between 1-100

   Arguemnts: Num: Length of list
   start_range: Starting numbers whihc will be 1
   end_range: Ending number which will be 100
   sort_list: If changed then the sort will be sorted

   Returns: t which is the list
   '''
   t = []

   if num <= 0:
      print('num must be > 0')

   # If num is not a int then it will print the following
   elif not isinstance(num, int):
      print('num must be an integer')

   # If start_range of end_range is not a int then it will print the following
   elif not isinstance(start_range, int) or not isinstance(end_range, int):
      print('start_range and end_range must be integers')

   # If everything is correct the follwing happens
   else:
      # Loops through the num value
      for i in range(num):

         # Uses the random module and grabs a random number between 1 and 100
         r = random.randint(start_range, end_range)

         # Adds that number to the list
         t.append(r)

      # If sort_list ever become 'Y' then the t list will be sorted
      if sort_list.upper() == 'Y':
         t.sort()

   return t
