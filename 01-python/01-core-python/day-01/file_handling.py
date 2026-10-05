from datetime import date
# ask the user and save the answer
learning = input("What did you learn? ")
minutes = input("How many minutes did you learn? ")
# Getting today's date
today = date.today()
# Append rather than overwrite previous entries.
with open("learnings.txt", "a") as file:
    # saving the entry in newline and adding the today's date
    file.write(f"{today} - {learning} | {minutes} minutes\n")
# Then read the entire file and print it.
print("\n--Learning Journal History--")
with open("learnings.txt", "r") as file:
    print(file.read())