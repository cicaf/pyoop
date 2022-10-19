#PROGRAMME THAT APPENDS A TEXT FILE WITH NAMES OF GUESTS...
file2 = 'guests.txt'

with open(file2,'a') as object4:
    name = input("What is your name sir: ")

    if name != 'quit':
        object4.write(name)

    else:
        print("we are done for today")


