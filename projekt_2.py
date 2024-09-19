"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lucie Černochová
email: cernochova.lucie@email.cz
discord: Lucie Č. (lucie.c123)
"""
import random
import time

def generate_random_number():
    """
    Vytvoří náhodné čtyřciferné číslo, které nezačíná 0 a číslice nejsou duplicitní.
    """
    number = random.sample(range(1, 10), 1)
    number += random.sample(range(0, 10), 3)
    
    while len(set(number)) != 4:
        number = random.sample(range(1, 10), 1) + random.sample(range(0, 10), 3)
  
    four_digits = ''.join(str(digit) for digit in number)
    return four_digits


def verify_player_guess(guess):
    """
    Ověří hráčem tipované číslo. Číslo nesmí mít jiné, než číselné znaky, 
    musí mít 4 číslice, nesmí začínat 0, číslice nesmí být duplicitní.
    """
    if not guess.isdigit(): 
        print("The number contains non-numeric characters!")
        return False
    elif len(guess) != 4:
        print("The number is shorter or longer than 4 digits!")
        return False
    elif guess[0] == "0":
        print("The number must not start with zero!")
        return False
    elif len(set(guess)) != len(guess):
        print("The number must not have duplicate values!")
        return False
    return True

def get_bulls_and_cows(secret_number, guess):
    """
    Vrátí počet bulls a cows na základě tajného čísla a tipovaného čísla.
    Bulls jsou čísla na správné pozici, Cows jsou správná čísla na nesprávné pozici.
    """
    bulls = 0
    cows = 0

    # Bulls - správná pozice čísla
    for i in range(4): 
        if secret_number[i] == guess[i]:
            bulls += 1

    # Cows - správné číslo na nesprávné pozici
    for i in range(4):
        if guess[i] in secret_number and guess[i] != secret_number[i]: 
            cows += 1

    return bulls, cows

def pluralize(count, word):
    """
    Vrátí správný tvar slova v závislosti na jednotném/množném čísle (bull/bulls nebo cow/cows).
    """
    if count == 1:
        return f"{count} {word}"
    else:
        return f"{count} {word}s"

game_statistics = []

def play_bulls_and_cows():
    print("Hi there!")
    print("-" * 50)
    secret = generate_random_number() 
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)
    attempts = 0
    # Začátek měření času.
    start_time = time.time()
    while True:
        guess = input("Enter a number: ")
        
        # Ověření hračem tipovaných čísel.
        if not verify_player_guess(guess):
            continue
        
        attempts += 1
        # Oveření správné pozice / správného čísla na nesprávné pozici.
        bulls, cows = get_bulls_and_cows(secret, guess)
        
        # Výpis výsledku s ohledem na jednotné/množné číslo.
        print(f"{pluralize(bulls, 'bull')}, {pluralize(cows, 'cow')}")
        print("-" * 50)
        
        if bulls == 4:
            # Konce měření času.
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print(f"Correct, you've guessed the right number {secret} in {attempts} guesses and {total_time} seconds!")
            
            # Uloží statistiky o hře.
            game_statistics.append((attempts, total_time))
            break
        

def main():  
    while True:
        play_bulls_and_cows()
        
        # Dotaz, zda chce hráč pokračovat.
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Výpis statistik.
    print("\nGame statistics:")
    for i, (attempts, total_time) in enumerate(game_statistics, 1):
        print(f"Game {i}: {attempts} attempts, {total_time} seconds")
    print("Thanks for playing!")

# Spuštění hry.
main()