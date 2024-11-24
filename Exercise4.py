#Primitive Quiz 
# step1-Write a program that asks the user "What is the capital of France?"
#  and waits for their response.
response = input("What is the capital of France? ")
#checking the answer of user
if response.lower() == "paris":
    print("Correct! The capital of France is Paris.")#if answer is correct
else:
    print("Wrong! The capital of France is Paris.")#if answer is not correct

#Advanced Requirements
# capitals of 10 European countries. 
quiz_data = {
    "France": "Paris",
    "Poland": "Warsaw",
    "Hungary": "Budapest",
    "Estonia": "Talinn",
    "Luxembourg": "Luxembourg",
    "Belgium": "Brussels",
    "Lithuania": "vinius",
    "Sweden": "Stockholm",
    "United kingdom": "London",
    "Austria": "Vienna"
}

# Programme to ask the question and check the answer
def ask_question(country, correct_answer):
    # Asking the user for the capital
    user_answer = input(f"What is the capital of {country}? ").strip()
    
    # accept answers regardless of the capitalization
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print("Wrong!")

def run_quiz():
    for country, capital in quiz_data.items():
        ask_question(country, capital)
run_quiz()

