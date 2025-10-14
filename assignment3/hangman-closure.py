#Task 4 

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        # using join
        result = ''.join([char if char in guesses else "_" for char in secret_word])
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
        if not guess:# added this two line to # Handle empty input 
            print("Please enter a guess.")
            continue
        if game(guess):
            print("You guessed the word!")
            break
