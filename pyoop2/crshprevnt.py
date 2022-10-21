#CRASH PREVENTION CODE...
#A SIMPLE DIVISION CALCULATOR
print("Please give us 2 numbers to devide...")
print("\n Enter q TO QUIT")

while True:
    firstnum = input("Please insert the first number :")
    if firstnum == 'q':
        break
    secondnum = input("Please give us the second number :")
    if secondnum == 'q':
        break
    else:
        ans = int(firstnum)/int(secondnum)

        print(f"{firstnum} devide {secondnum} is {ans} ")