file = 'pi_digits.txt'

file2 = '' #AN EMPTY STRING TO STORe OUR PRODUCT
with open(file) as object1:
    lines = object1.readlines()  #SEPARATES IT INTO DIFFERENT LINES

for line in lines:
    file2 += line.rstrip()

print(file2)
