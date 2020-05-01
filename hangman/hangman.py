import csv
import random

wrong_guess_count = 0
wrong_guesses = set()
correct_guesses = set()
hangman_states = {
    0: """
    :)
    """,
    1: """
    (x_x)
    """,
    2: """
    (x_x)
      |
    """,
    3: """
    (x_x)
    / |
    """,
    4: """
    (x_x)
    / | \\
    """,
    5: """
    (x_x)
    / | \\
     /
    """,
    6: """
    (x_x)
    / | \\
     / \\
    """
}

def check_for_letter(string, letter):
    for char in string:
        if char == letter:
            return True
    return False

def enumerate_letters(string, letter):
    return [i for i, char in enumerate(string) if char == letter]

def replace_letters(string, indexes, guess):
    s = ''
    replacer = list(string)
    for index in indexes:
        replacer[index] = guess
    return(s.join(replacer))
      
challenge = ''

#fuck this code its so useless
with open('hangman/most-common-nouns-english.csv') as wordlist:
    listreader = csv.reader(wordlist)
    wordlist = list(listreader) #converts the csv file into a list
    randomnum = random.randint(1, len(wordlist)) 
    preprocessed = str(wordlist[randomnum]) #randomly picks a word
    nextstring=preprocessed[2:] #trims the word
    challenge=nextstring[:-2]

hidden_challenge = '*'*len(challenge)
print('welcome to hangman!')
print('a word has been chosen:')
print(hidden_challenge)
print(challenge)
print('guess what it is!')

while hidden_challenge != challenge and wrong_guess_count < 6:
    while True:
        guess = str(input('take a guess: '))
        if guess == challenge:
            hidden_challenge = guess
            break
        elif len(guess) > 1:
            print('oi, guess ONE letter.')
        elif guess in correct_guesses or guess in wrong_guesses:
            print('you already guessed that.')
        else:
            break
    
    if hidden_challenge == challenge:
        break

    if check_for_letter(challenge, guess):
        print('you guessed correctly!')
        occurrences = enumerate_letters(challenge, guess)
        hidden_challenge = replace_letters(hidden_challenge, occurrences, guess)
        print(hidden_challenge)
        correct_guesses.add(guess)
    else:
        print('sorry, that\'s wrong.')
        wrong_guesses.add(guess)
        wrong_guess_count += 1
        print(hangman_states[wrong_guess_count])

if(hidden_challenge == challenge and wrong_guess_count < 6):
    print('congrats! you win!')
else:
    print('sorry, better luck next time.')
