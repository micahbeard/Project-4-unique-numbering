"""
Project 4: unique numbering:
Take a user file input
Read in a file of numbers
Find min, max, mean, sum
Find the number that repeats the most
Write results to new unique output file
"""

from statistics import mean
from statistics import multimode
import time

# Input File
usr_file_input = input("Enter File: ")
timestr = time.strftime("Output-%Y_%m_%d-%H_%M_%S")
largestInt = 0 
smallestInt = 0

# Opening file 
with open(usr_file_input) as f:
    numbers = f.read().splitlines()

# Print Whole List
print("numbers: ",numbers)

# Math
numbers = [int(i) for i in numbers]
largestInt = max(numbers)
smallestInt = min(numbers)
meanInt = mean(numbers)
addInt = sum(numbers)
modeInt = multimode(numbers)

# Var for Output File
out_print_list = ["Largest Int:", largestInt, "Smallest Int:", smallestInt, "Mean of Int:", meanInt, "Addition of all Int:", addInt, "Most Common Int:", modeInt]

# Terminal Print
print("numbers: ",numbers)
print("Smallest number: ", smallestInt)
print ("Largest number:  ", largestInt)
print("Mean of numbers: ", meanInt) 
print("Addition of all number: ", addInt)
print("Most Common Number: ", modeInt)

# Writing to File
out_print = open(timestr, 'w')
print(timestr)
out_print.write(str(out_print_list))
