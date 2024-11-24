
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_name = "Sam"
if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")

    #Optional Requirements:
search_name = input("Enter the name to search for: ")
if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was not found in the list.")

