# CIS 122 Fall 2020 Assignemnt 5
# Author: Karma Woeser
# Partner: Your Partner
# References:
# Description: Guess problem

guess_count = 0
letters_guessed = ''
matched_letters = ''
unmatched_letters = ''


guess_word = input("Enter a word(Blank to quit): ")

def check(word_checked, letter):
    '''Purpose: Checks to see if the guessed letter is in the word. Also is used to check
    for characters that show up more then once.

    Args: word is guess_word that is inputted at the start
    letter is the guess_letter that is in the while loop

    Returns: Total, based on the amount of times the letter appears in the word
    '''      
    total = 0
    for multiple in word_checked:
        if multiple == letter:
            total += 1

    return total


while True:
    guess_letter = input('Enter a guess letter(blank to quit):')
    guess_count += 1
    letter_check = check(guess_word, guess_letter)

    # If the input of guess letter is > 1 then nothing will happen expect a print statement
    if len(guess_letter) > 1:
        print('\t> Only enter a single letter')


    # If the input of guess letter is nothing the it will just end the loop and print the results 
    elif len(guess_letter) == 0:
        print('> All letters found' ,
              '\n***Results***' , '\nWord:\t\t',guess_word,
              '\nMatched:\t',matched_letters ,
              '\nUnmatched:\t',unmatched_letters ,
              '\nGuesses:\t',guess_count)
        break

    # If their are no letters found in the word it will do the following
    elif letter_check == 0:
        unmatched_letters += guess_letter
        letters_guessed += guess_letter
        print('\t> ' + guess_letter + ' not found')
        print('\t> Guesses so far: ' + letters_guessed)

    # If guess_letter has already been matched with the word then it will not do anything
    # But print the following print statements
    elif guess_letter in matched_letters:                                                                                    
            print('\t> Letter has already been guessed and found')
            print('\t> Guesses so far: ' + letters_guessed)
        
    # If guess_letter has already been checked and wasn't found in the word it will just
    # Print the following 
    elif guess_letter in unmatched_letters:
            print('\t> Letter has already been guessed and not found')
            print('\t> Guesses so far: ' + letters_guessed)
            
    # If their is 1 letter that is found in the word then it will do the following
    elif letter_check == 1:
        matched_letters += guess_letter 
        letters_guessed += guess_letter
        print('\t> '+ guess_letter + ' found')
        print('\t> Guesses so far: ' + matched_letters + unmatched_letters)

    # If there is more then 1 letter found in the word then it will do the following
    elif letter_check > 1:
        print('\t> ' + guess_letter + ' found')
        print('\t> Guesses so far: ' + letters_guessed)
        for amount in range(letter_check):
            matched_letters += guess_letter
        letters_guessed += guess_letter
        
    # Once the length of matched letters is equal to the length of the word it will do the following
    if len(matched_letters) == len(guess_word):
        print('> All letters found' ,
              '\n***Results***' , '\nWord:\t\t',guess_word,
              '\nMatched:\t',matched_letters ,
              '\nUnmatched:\t',unmatched_letters ,
              '\nGuesses:\t',guess_count)
        break



            
        
