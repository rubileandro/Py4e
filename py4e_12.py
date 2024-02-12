"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
file_name = 'mbox-short.txt'

email_counts = {}

try:
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                email_counts[email] = email_counts.get(email, 0) + 1
except FileNotFoundError:
    print(f"The file {file_name} was not found.")

max_count = None
max_email = None

for email, count in email_counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(max_email, (max_count))
