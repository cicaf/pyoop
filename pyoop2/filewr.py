#TEACHING ON FILE WRITTING USING OPEN AND 'w'
filename = 'wrote.txt'

with open(filename,'w') as object2:
    object2.write("it will obviously work...its all about practice...and getting better..its stressfull though")

with open(filename,'a') as object3:
    object3.write('\n We have all been through this same thing...\n the singing part...im day dreaming,let me count the ways,how ill get you oh and how ill make you pay')
    