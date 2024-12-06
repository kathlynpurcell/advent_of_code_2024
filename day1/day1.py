import sys

# get the data
ex_data = open("day1_ex.txt", "r").readlines()
data = open("day1_data.txt", "r").readlines()

# let the user specify 'example' or any arg... which will default to example
if len(sys.argv) == 2: 
	data = ex_data

# break up the columns, or 'lines'
first_line = [int(i.split()[0]) for i in data]
second_line = [int(i.split()[1]) for i in data]

# sort them for the calculations
sorted1 = sorted(first_line)
sorted2 = sorted(second_line)

# add the difference between the sorted values
total1 = 0
for i in range(len(sorted1)):
	total1 += abs(sorted1[i] - sorted2[i])

# tell the user the answer for part 1
print("The result of the sorted differences are: ", total1)

## part 2
total2 = 0
# for each item in the first line multiply it by
## the number of times it appears in the second line
## and add it to the total
for number_one in first_line:
	total2 += number_one*second_line.count(number_one)

print("The result of the first element appearing in the second column is: ", total2)