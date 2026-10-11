import random


play_again = "yes".strip().lower()

while play_again == "yes":
    secret = random.randint(1,25)
    attempts = 0
    max_attempts = 5

    print("===Guess the number====")
    print("Guess a number between 1 and 100")
    print(f"You have {max_attempts} attempts")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))

        except ValueError:
            print("Please enter a valid number")
            continue

        attempts += 1

        if guess == secret:
            print(f"\nYou got it in {attempts} attempts!")
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")

    remaining = max_attempts - attempts

    if remaining > 0:
        print(f"\nYou have {remaining} attempts")

    else:
        print("You have no attempts left!!")
        print(f"\nThe number was {secret}")

    play_again = input("\nPlay Again? (yes/no): ").strip().lower()
    print(play_again)

    if play_again == "yes":
        print("Lets Go!!")
    else:
        print("Goodbye!")















