#CODE TO TRY EXCEPT AND ELSE ourselves into finding and troubleshooting an error

filename = "alice_in_wonderland.txt"

try:
    with open (filename,encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("File doesnt exist baratna")

else:
        #TO COUNT THE TOTAL NUMBER OF WORDS IN THE FILENAME
        wording = content.split()
        no_of_words = len(wording)

        print(f"The total number of words in the text is {no_of_words}")

