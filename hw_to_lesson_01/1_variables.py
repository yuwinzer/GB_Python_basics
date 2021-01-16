number = 16
print(f"This is an integer type of number: {int(number)}")
print(f"This is a float type of number: {float(number)}")
print("Now type your numbers and text. I will print it in different types!")
user_number_1 = int(input("\nType first number here: "))
user_number_2 = int(input("Type second number: "))
user_text_1 = input("Now type some text: ")
user_text_2 = input("And type any text  again: ")
print(f"This is an integer type of your numbers: {int(user_number_1)} and {int(user_number_2)}")
print(f"This is a float type of your numbers: {float(user_number_1)} and {float(user_number_2)}")
list_type = [user_number_1, user_number_2, user_text_1, user_text_2]
print(f"This is all your inputs in a list type: {list_type}")
