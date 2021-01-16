input_number = input("Type any positive number with more than 1 digits: ")
list_of_input_numbers = list(input_number)

i = 1
max_digit = list_of_input_numbers[0]
while i < len(input_number):
    if list_of_input_numbers[i] > list_of_input_numbers[i-1]:
        max_digit = list_of_input_numbers[i]
    i += 1
print(f"Maximal digit in your number is {max_digit}")
