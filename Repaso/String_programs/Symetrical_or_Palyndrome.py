def symetrical_or_palyndrome(word):
    word=word.casefold().replace(" ","")
    reverse_word=word[::-1]
    if word==reverse_word:
        print(f"{word} is a palyndrome")
    else:
        print(f"{word} is not a palyndrome")
    half=len(word)/2
    if len(word)%2==0:
        first_half=word[:int(half)]
        second_half=word[int(half):]
        if first_half==second_half:
            print(f"{word} is symetrical")
        else:
            print(f"{word} is not symetrical")
    else:
        print(f"{word} is not symetrical")





symetrical_or_palyndrome(input("Enter a word to check if is palyndrome or symetrical: "))

print(5/2)