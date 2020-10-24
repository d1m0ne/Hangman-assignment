import random
from random import randrange 
import urllib.request

def choose_word():
    file_name = "https://raw.githubusercontent.com/d1m0ne/Hangman-assignment/main/Words%20for%20Hangman.txt"
    my_file = urllib.request.urlopen(file_name)
    long_string = my_file.read()
    long_string = long_string.decode("utf-8")
    word_list = long_string.split("\n")
    word = word_list[randrange(714)]
    word = word[0:len(word)-1]
    return word

def initial_blanks(word):
    word_list = []

    for num in range(len(word)):
        word_list.append("_")
    return word_list

def divide_word(word):
    word_char = []
    word_char[:0] = word
    return word_char
    
def check_word(word_chars, letter):
    for b in range(len(word_chars)):
        if letter == word_chars[b]:
            return True
    return False

def ask_letter():
    is_letter = False
    while is_letter == False:
        print("Please enter a letter that belongs to the hidden word. This message will repeat if you enter something other than a letter")
        choice = input().lower()
        if choice.isalpha() == True:
            return choice

def correct_guess(chosen_letter, chosen_word, word_list):
    for i in range(len(word_list)):
        if chosen_letter == chosen_word[i]:
            word_list[i] = chosen_letter
    return word_list

def check_for_win(blanks):
    for l in range(len(blanks)):
        if blanks[l] == "_":
            return False
    return True

def incorrect_guess(number, wrong_guesses):
    if number == 1:
        print(" __")
        print("|  |")
        print("|  |")
        print("|  |")
        print("|  (_)  ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("That letter is not part of the word.")
        print()
        print("These are your wrong guesses so far ", wrong_guesses)
    if number == 2:
        print(" __")
        print("|  |")
        print("|  |")
        print("|  |")
        print("|  (_)  ")
        print("|   |   ")
        print("|   |   ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("That letter is not part of the word.")
        print()
        print("These are your wrong guesses so far ", wrong_guesses)
    if number == 3:
        print(" __")
        print("|  |")
        print("|  |")
        print("|  |")
        print("|  (_)  ")
        print("|  /|   ")
        print("| / |   ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("That letter is not part of the word.")
        print()
        print("These are your wrong guesses so far ", wrong_guesses)
    if number == 4:
        print(" __")
        print("|  |")
        print("|  |")
        print("|  |")
        print("|  (_)  ")
        print("|  /|\  ")
        print("| / | \ ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("That letter is not part of the word.")
        print()
        print("These are your wrong guesses so far ", wrong_guesses)
    if number == 5:
        print(" __")
        print("|  |")
        print("|  |")
        print("|  |")
        print("|  (_)  ")
        print("|  /|\  ")
        print("| / | \ ")
        print("|  /    ")
        print("| /     ")
        print("|")
        print("|")
        print("|")
        print("That letter is not part of the word.")
        print()
        print("These are your wrong guesses so far ", wrong_guesses)
    if number == 6:
        print(" __")
        print("|  |")
        print("|  |")
        print("|  |")
        print("|  (_)  ")
        print("|  /|\  ")
        print("| / | \ ")
        print("|  / \  ")
        print("| /   \ ") 
        print("|")
        print("|")
        print("|")
        print("That letter is not part of the word.")
        print()
        print("These are your wrong guesses so far ", wrong_guesses)

word = choose_word()

divided_word = divide_word(word)

initial_list = initial_blanks(word)

win_condition = False

lose_condition = False

wrong_guess = 0

wrong_guesses = []

while (win_condition == False) and (lose_condition == False):
    current_letter = ask_letter()
    if check_word(divided_word, current_letter) == True:
        initial_list = correct_guess(current_letter, divided_word, initial_list)
        print(initial_list)
    elif check_word(initial_list, current_letter) == False:
        wrong_guesses.append(current_letter)
        wrong_guess += 1
        incorrect_guess(wrong_guess, wrong_guesses)
        print(initial_list)
    if check_for_win(initial_list) == True:
        win_condition = True
        break
    elif wrong_guess == 6:
        lose_condition = True
        break

if win_condition == True:
    print("You have guessed the whole word!")

if lose_condition == True:
    print("You are out of guesses! The word was " + word)