"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except 
and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
"""

int_list = []

while True:
    user_input = input("Please provide an integer: ")
    if user_input.lower() == "done":
        break
    else:
        try:
            num = int(user_input)
            int_list.append(num)
        except ValueError:
            print("Invalid input")


max_int = max(int_list)
min_int = min(int_list)
print(f'Maximum is {max_int}')
print(f'Minimum is {min_int}')
