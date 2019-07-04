import random
import sys
x = random.randint(1,5)

input_number = input("Guess goes here: ")
try:
    input_number=int(input_number)
except ValueError:
    print("error occurred")
    sys.exit()
    

while x != input_number:
    print(input_number)
    print("incorrect")
    try:
        input_number = int(input("Guess again: "))
    except ValueError:
        print("error occurred")
        sys.exit()
    

print("correct!!")

