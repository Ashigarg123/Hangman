import random

my_list = ["Cat", "Dog", "Mumbai", "India"]
# A radom word will e choose from the above list
def hangman(word):
    wrong = 0
    stages = ["",
              "________          ",
              "|                  ",
              "|         |        ",
              "|         O        ",
              "|       / | \      ",
              "|        / \       ",
              "|                  "
              ]
    rletters = list(word)
    #storing letters from the word in rletters list.
    board = ["_"] * len(word)
    # Showing the user how many letters are there, for it storing the board
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        # Asking the user to guess till the whole hangman forms.
        msg = "Guess a letter"
        char = input(msg)
        #If the input letter is in the word. Update the board
        if char in rletters:
            cind = rletters.index(char)
            #we are getting the index of the character from our board
            board[cind] = char
            #then replacing the underscore with the character.
            rletters[cind] = "$"
            #however index returns only the first index of the character we look for, so code will not work if the word has more than one of the same characters. Therefore replacing the character which was guessed correctly by $
        else:
            wrong += 1
            #If player guesses incorrect letter, increment wrong by 1.
        print((" ".join(board)))
        #Now print the updated board
        e = wrong + 1
        print("\n".join(stages[0: e]))
        #for every wrong answer print the hangman till the list is complete.(Or the hangman is fully formed)
        #finally if there is no more blank spaces in the board. Declare the user as winner.
        if "_" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break
        if not win:
            print("\n".join(stages[0: wrong]))
            #
p=random.choice(my_list)
hangman(p)
print("You lose! It was {}.".format(p))
