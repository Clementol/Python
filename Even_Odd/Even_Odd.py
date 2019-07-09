"""
By Clement
Phone: 08167515092
"""
all_numbers = [] #Empty list of all numbers

#To enter the length of numbers
n = int(input("How many numbers: "))

#To print the length of numbers
print("Enter any", n, "numbers")

#Loop To input the arrays of numbers according to the length and
#put it in all_numbers list
for i in range(1, n+1):
    arr = int(input('{}-- '.format(i)))
    all_numbers.append(arr) #
#array of all even numbers
even_numbers = []
#array of all odd numbers
odd_numbers = []

#Loop to seperate all_number into even and odd lists
for j in all_numbers:
    if j % 2 == 0:
        even_numbers.append(j)
    else:
        odd_numbers.append(j)

#To print out all even numbers
print("Even numbers are:", )
for i in range(len(even_numbers)):
    print(i+1, "\b.", even_numbers[i])
if len(even_numbers) == 0:
    print("\tNo even numbers")
        
#Loop to print out all odd numbers
print("Odd numbers are:")
for i in range(len(odd_numbers)):
    print(i+1, "\b.", odd_numbers[i])
if len(odd_numbers) == 0:
    print("\tNo odd numbers")