import re 
import sys

# get the data
ex_data = open("day3_ex.txt", "r").readlines()
data = open("day3_data.txt", "r").readlines()

# let the user specify 'example' or any arg... which will default to example
if len(sys.argv) == 2: 
	data = ex_data

pattern = re.compile(r'mul\(([0-9]+)\,([0-9]+)\)')

total = 0
total_pt1 = 0
corrupted = "".join(data)
corrupted_dos = re.sub(r'(?s)don\'t\(\).*?do\(\)[^\w\s]*', 'dontkaseydo', corrupted)
# simple solution to remove final dont if applicable
corrupted_dos = corrupted_dos.split("don\'t()")[0]

for (mult1, mult2) in re.findall(pattern, corrupted):
	total_pt1 += (int(mult1)*int(mult2))

for (mult1, mult2) in re.findall(pattern, corrupted_dos):
	total += (int(mult1)*int(mult2))

print("Pt1: ", total_pt1)
print("Pt2: ", total)