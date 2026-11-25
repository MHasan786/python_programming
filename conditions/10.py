# Check whether a character is a vowel or consonant.

check_vowel = (input("Enter a character here: "))

if len(check_vowel) == 1 and check_vowel.isalpha:
    if check_vowel in "AaEeIiOoUu":
        print("The given character is a vowel:", check_vowel)
    else:
        print("The given character is a consonant:", check_vowel)
else:
    print("Please enter a single valid letter.")