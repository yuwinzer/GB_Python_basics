input_time = int(input("Type your time in seconds: "))
print(f"\nYou entered {input_time} seconds")
hours = input_time // 3600
minutes = input_time // 60 - hours * 60
seconds = input_time - hours * 3600 - minutes * 60
print(f"Your time will be: {hours:02d}:{minutes:02d}:{seconds:02d}")