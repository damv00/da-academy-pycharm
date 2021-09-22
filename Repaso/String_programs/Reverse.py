#Reverse words in a given String in Python
stri = "geeks quiz practice code"
x=stri.split(" ")
x.reverse()
x=" ".join(x)
print(x)

name = "Edson"
lista = []
var=""
for i in name:
    var=i+var
print(var)

value = input("Think of a number between 0 and 100!: ")
print(f"Is your secret number {value / 2}?")
validation = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
if validation == "l":
    value = ((value / 2) + value) / 2
    print(f"Is your secret number {value}?")
    validation = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
elif validation == "h":
    value = (value / 2)
elif validation == "c":
    print("Game over. Your secret number was: {value/2}"
    else:
    print("Sorry, I did not understand your input.")
