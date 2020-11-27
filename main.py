import random

WORDLIST_FILENAME = "words.txt"
def load_words(WORDLIST_FILENAME):

    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):

    return random.choice(wordlist)

# створення слова
wordlist =  ((load_words(WORDLIST_FILENAME)))
secret_word  = choose_word(wordlist)


def is_word_guessed( secret_word, letters_guessed) :
    secret_word = list(secret_word)
    my_word = ("* " * len(secret_word)).split(" ")
    del my_word[-1]
    for i in letters_guessed:
        for a in secret_word:
            if a == i:
                indices = [a for a, x in enumerate(secret_word) if x == i]
                for b in indices:
                    my_word[b] = secret_word[b]
    if  my_word == secret_word :
        print("Congratulations, you won!" ,"\n", "Your total score for this game is :" ,len(letters_guessed)*len(secret_word))


def get_guessed_word(secret_word, letters_guessed):
    secret_word = list(secret_word)
    my_word = ("_ "*len(secret_word) ).split(" ")
    del my_word[-1]
    for i in letters_guessed:
        for a in secret_word  :
            if a == i :
                indices = [a for a, x in enumerate(secret_word ) if x == i ]
                for b in indices :
                  my_word[b] = secret_word[b]


    for r in my_word:
      print(" " , r, end = '' )
    return  my_word


def get_available_letters(letters_guessed):
    alfabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_guessed = set(letters_guessed )
    available_letters =  alfabet - letters_guessed
    print("\n" , "Available letters: " )
    for r in available_letters:
        print(r, end=' ')
    return available_letters

def hangman(secret_word):
    number_of_tryies = 6
    print("I am thinking of a word that is ", len(secret_word) , " letters long. ")
    print("You have", number_of_tryies,  ", guesses left ")
    secret_word = list(secret_word)
    number_of_failse = 0
    letters_guessed =[]
    available_letters =set('abcdefghijklmnopqrstuvwxyz')
    while True :
      letter_guessed = str(input("Please guess a letter: ")).lower()
      letters_guessed.append(letter_guessed)
      if letter_guessed not in  available_letters and letter_guessed not in 'a, e, i, o, u, b, c, d, f, g, h, j, k, l, m, n, p , q, r, s, t, v, x, z, y'.split(", "):
          number_of_failse = number_of_failse + 1
          get_available_letters(letters_guessed)
          print("Oops! That is not a valid letter. You have  ", 3-number_of_failse , "warnings left:" )
          print("\n","---------------------------------------------------")
      if letter_guessed not in available_letters and letter_guessed  in 'a, e, i, o, u, b, c, d, f, g, h, j, k, l, m, n, p , q, r, s, t, v, x, z, y'.split( ", "):
          number_of_failse = number_of_failse + 1
          get_available_letters(letters_guessed)
          print("Oops! You've already guessed that letter. You now have ", 3 - number_of_failse, "warnings left:")
          print("\n", "---------------------------------------------------")
      if  number_of_failse == 3 :
          number_of_tryies = number_of_tryies - 1
      if letter_guessed not in  secret_word and letter_guessed  in 'a, e, i, o, u'.split(", ") and letter_guessed  in available_letters :
         number_of_tryies = number_of_tryies  - 2
         print("Oops! That letter is not in my word:")
         get_guessed_word(secret_word, letters_guessed)
         get_available_letters(letters_guessed)
         print("\n","---------------------------------------------------")
      if letter_guessed not in  secret_word and letter_guessed  in 'b, c, d, f, g, h, j, k, l, m, n, p , q, r, s, t, v, x, z, y'.split(", ") and letter_guessed  in available_letters :
         number_of_tryies = number_of_tryies  -1
         print("Oops! That letter is not in my word:")
         get_guessed_word(secret_word, letters_guessed)
         get_available_letters(letters_guessed)
         print("\n","---------------------------------------------------")
      if letter_guessed in secret_word and letter_guessed in available_letters:
          get_guessed_word(secret_word, letters_guessed)
          get_available_letters(letters_guessed)
          is_word_guessed(secret_word, letters_guessed)
          print("\n","---------------------------------------------------")
      if number_of_tryies > 0:
              print(" You have", number_of_tryies,  ", guesses left ")
      if number_of_tryies <= 0:
          print(" Sorry, you ran out of guesses. The word was : ", secret_word)
          break



def match_with_gaps(my_word, other_word):
    if len(my_word) != len(other_word):
        return False

    pos = 0
    letters = set()

    while pos < len(my_word):
        if my_word[pos] == '_':
            letters.add(other_word[pos])
        elif my_word[pos] != other_word[pos]:
            return False
        pos += 1

    if len(letters & set(my_word)) > 0:
        return False

    return True


def show_possible_matches(my_word):
    print("\n ","Possible word matches are:")
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=' ')


def hangman_with_hints(secret_word):
    print(secret_word)
    number_of_tryies = 6
    print("I am thinking of a word that is ", len(secret_word), " letters long. ")
    print("You have", number_of_tryies, ", guesses left ")
    secret_word = list(secret_word)
    number_of_failse = 0
    letters_guessed = []
    available_letters = set('abcdefghijklmnopqrstuvwxyz')

    while True:
        letter_guessed = str(input("Please guess a letter: ")).lower()
        letters_guessed.append(letter_guessed)

        if letter_guessed not in available_letters and letter_guessed not in 'a, e, i, o, u, b, c, d, f, g, h, j, k, l, m, n, p , q, r, s, t, v, x, z, y'.split(", ") and letter_guessed != "*":
            number_of_failse = number_of_failse + 1
            get_available_letters(letters_guessed)
            print("Oops! That is not a valid letter. You have  ", 3 - number_of_failse, "warnings left:")
            print("\n", "---------------------------------------------------")
        if letter_guessed not in available_letters and letter_guessed in 'a, e, i, o, u, b, c, d, f, g, h, j, k, l, m, n, p , q, r, s, t, v, x, z, y'.split(", "):
            number_of_failse = number_of_failse + 1
            get_available_letters(letters_guessed)
            print("Oops! You've already guessed that letter. You now have ", 3 - number_of_failse, "warnings left:")
            print("\n", "---------------------------------------------------")
        if number_of_failse == 3:
            number_of_tryies = number_of_tryies - 1
        if letter_guessed not in secret_word and letter_guessed in 'a, e, i, o, u'.split(
                ", ") and letter_guessed in available_letters:
            number_of_tryies = number_of_tryies - 2
            print("Oops! That letter is not in my word:")
            get_guessed_word(secret_word, letters_guessed)
            get_available_letters(letters_guessed)
            print("\n", "---------------------------------------------------")
        if letter_guessed not in secret_word and letter_guessed in 'b, c, d, f, g, h, j, k, l, m, n, p , q, r, s, t, v, x, z, y'.split(
                ", ") and letter_guessed in available_letters:
            number_of_tryies = number_of_tryies - 1
            print("Oops! That letter is not in my word:")
            get_guessed_word(secret_word, letters_guessed)
            get_available_letters(letters_guessed)
            print("\n", "---------------------------------------------------")

        if letter_guessed in secret_word and letter_guessed in available_letters:
            get_guessed_word(secret_word, letters_guessed)
            get_available_letters(letters_guessed)
            is_word_guessed(secret_word, letters_guessed)
            print("\n", "---------------------------------------------------")
        if letter_guessed == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

            print("\n", "---------------------------------------------------")
        if number_of_tryies > 0:
            print(" You have", number_of_tryies, ", guesses left ")
        if number_of_tryies <= 0:
            print(" Sorry, you ran out of guesses. The word was : ", secret_word)
            break

if __name__ == "__main__":
    print("Welcome to the game Hangman! ")

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)


