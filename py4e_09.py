"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form: "X-DSPAM-Confidence: 0.8475"
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
file_name = input("Please provide a file name: ")

line_count = 0
total = 0

with open(file_name) as file:
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            line_count += 1

            colon_pos = line.find(':')
            number_str = line[colon_pos+1:].strip()
            number = float(number_str)
            total += number

if line_count > 0:
    average = total / line_count
    print(f'Average spam confidence: {average}')
else:
    print('No matches found in the file.')
