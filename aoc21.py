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
       lowNum = min(results)
       highNum = max(results)
       diff = highNum - lowNum
       diffSum += diff


print(diffSum)