# AoC Day 2 Solution by Cihad Colak
# Entered the input as a file


# Open File
with open('aoc21.txt') as f:
   diffSum = 0

   # Cycle through lines
   for line in f:
       # Convert line to List of strings
       lineList = line.split()
       # Convert each string into a int
       results = list(map(int, lineList))


       # Circle through results
       # 2 for loops to compare each number with
       # every other number in the line
       for num in results:
           for num2 in results:
               if num == num2:
                   continue
               elif num % num2 == 0:
                   diffSum += int(num / num2)





print(diffSum)