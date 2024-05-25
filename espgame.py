import random

def play_game():
    score = 0
    for round in range(1, 11):
        secret_number = random.randint(1, 5)
        print("Round", round)
        guess = int(input("Guess the secret number (between 1 and 5): "))
        
        if guess == secret_number:
            print("Correct!")
            score += 1
        else: 
            print("Incorrect! The secret number was:", secret_number)
    
    return score

def main():
    print("Welcome to the ESP Trainer!")
    print("You will have to guess the secret number in each round.")
    print("Let's begin!\n")

    score = play_game()

    print("\nGame Over!")
    print("Your score:", score)

    if score >= 0 and score <= 2:
        print("Try again!")
    elif score >= 3 and score <= 4:
        print("Moderately Psychic")
    elif score >= 5 and score <= 6:
        print("Above Average Psychic")
    elif score >= 7 and score <= 8:
        print("Extra Sensory Powers Detected")
    elif score >= 9 and score <= 10:
        print("ESP WIZARD")

if __name__ == "__main__":
    main()
