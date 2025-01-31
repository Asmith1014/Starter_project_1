print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n"))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = float(input("How many people will be splitting the bill?\n"))
percentage2 = (percentage/100)*total_bill
total_with_tip = total_bill + percentage2
final_total =round((total_with_tip/people),2)
final_total = "{:.2f}". format(final_total)
print(f"Each person should pay {final_total}")