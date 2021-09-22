#Check if a string is a palindrome or not

def palindrome(word):
    word=word.casefold().replace(" ","")
    reverse_word=word[::-1]
    if word==reverse_word:
        print("True")
    else:
        print("False")

palindrome(input("Enter a string to check if is palindrome or not: "))