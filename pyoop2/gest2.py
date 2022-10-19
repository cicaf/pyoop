"""
Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""
active = True

filex = ('guest_book.txt')

with open (filex,'a') as object5:
    while active:
        name = input("please what is your name: \n \n \n")
        if name != 'quit':
            print(f"Welcome to our resort {name} enjoy your stay here ")
            object5.write(name)
        else:
            active = False
            break