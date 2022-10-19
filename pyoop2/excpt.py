#THIS GIVES A ZERODIVISION ERROR...

w = 100/0
print(w)

#Implementation of except and try blocks


try:
    x = 99/0
    print(x)
except ZeroDivisionError:
        print("Cannt devide by chocu sorry by zerhhoo....")
