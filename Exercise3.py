#biography
# Step 1: Store the information as key-value pairs in a dictionary
person_info = {
    'name': 'Riza Thayyil',
    'hometown': 'Kannur,Kerala',
    'age': 18
}
# Step 2: Print the values on separate lines using a single print() statement
print(person_info['name'])
print(person_info['hometown'])
print(person_info['age'])

#advanced requirments
#Have the user input their name, hometown, and age instead of hardcoding the values
name=input("Enter your name:")
hometown=input("Enter your hometown:")
# Testing the program by entering a string value for age (e.g., "eighteen").
while True:
    age_input = input("Please enter your age: ")
    try:
        age = int(age_input)
        break  
    except ValueError:
        print(f"'{age_input}' is not a valid number. Please enter a valid number for age.")
    

