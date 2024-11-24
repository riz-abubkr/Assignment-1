# Define a dictionary where the keys are month numbers and the values are the number of days in those months
months_days = {
    1: 31, 
    2: 28,   
    3: 31,  
    4: 30,   
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,   
    9: 30,   
    10: 31,  
    11: 30,  
    12: 31   
}

# Input Handling: Ask the user to input the month number.
month_number = int(input("Enter the month number (1-12): "))

# Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
if 1 <= month_number <= 12:
    print(f"The month number {month_number} has {months_days[month_number]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")


    #Advanced Requirement:
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

if month_number == 2:
    year = int(input("Enter the year to check for leap year: "))
    if is_leap_year(year):
        months_days[2] = 29  

