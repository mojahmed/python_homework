#Task 4 

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        # it dosent have to be letter i can chose any word in the my terminal 
        guesses.append(letter)
        result = ""
        for char in secret_word:
            if char in guesses:
                result += char
            else:
                result += "_"
        print(result)
        return "_" not in result

    return hangman_closure

#############
if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    game = make_hangman(secret)

    print("Start guessing letters!")
    while True:
        guess = input("Guess a letter: ")
        if game(guess):
            print("You guessed the word!")
            break
