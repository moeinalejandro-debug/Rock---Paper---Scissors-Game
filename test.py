
import random
import time

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

CHOICES = ["rock", "paper", "scissors"]
ALIASES = {"r": "rock", "p": "paper", "s": "scissors"}

BEATS = {
    "rock": {"scissors"},
    "paper": {"rock"},
    "scissors": {"paper"},
}


def show_score(user_score, computer_score):
    print(f"\nYour score: {user_score} | Computer score: {computer_score}")


def final_result(name, user_score, computer_score, rounds):
    print("\n" + "=" * 35)
    print(f"Rounds played: {rounds}")
    print(f"{name}'s score: {user_score}")
    print(f"Computer's score: {computer_score}")
    print("=" * 35)

    if user_score > computer_score:
        print(f"{BOLD}{GREEN}YOU WON THE GAME!{RESET}")
    elif user_score < computer_score:
        print(f"{BOLD}{RED}YOU LOST THE GAME!{RESET}")
    else:
        print(f"{BOLD}{YELLOW}IT'S A TIE!{RESET}")


def get_name():
    while True:
        name = input("What is your name? ").strip()

        if name:
            return name.capitalize()

        print("Name cannot be empty. Please try again.")


def main():
    name = get_name()
    user_score = 0
    computer_score = 0
    rounds = 0

    print(f"\nWelcome, {name}!")
    print("Type rock, paper, scissors, or quit.")
    print("You can also use r, p, or s.\n")

    while True:
        user_raw = input("Rock, paper or scissors? ").lower().strip()

        if user_raw == "quit":
            print("\nLeaving the game...")
            final_result(name, user_score, computer_score, rounds)
            break

        if user_raw not in CHOICES and user_raw not in ALIASES:
            print("Invalid choice! Try rock, paper, scissors, or quit.")
            continue

        user = ALIASES.get(user_raw, user_raw)
        computer = random.choice(CHOICES)
        rounds += 1

        print(f"\nYour choice: {user}")
        print(f"Computer's choice: {computer}")

        time.sleep(0.5)

        if user == computer:
            time.sleep(2)
            print(f"{BOLD}{YELLOW}IT'S A TIE!{RESET}")

        elif computer in BEATS[user]:
            time.sleep(2)
            print(f"{BOLD}{GREEN}YOU WON!{RESET}")
            user_score += 10

        else:
            time.sleep(2)
            print(f"{BOLD}{RED}YOU LOST!{RESET}")
            computer_score += 10

        time.sleep(2)
        show_score(user_score, computer_score)
        print("-" * 40)

        while True:
            repeat = input(
                "Continue? (yes/no/see): "
            ).lower().strip()

            if repeat in ("yes", "y"):
                print("\nLet's play again!\n")
                break

            elif repeat in ("no", "n"):
                print("Goodbye!")
                return

            elif repeat in ("see", "see the final result"):
                final_result(
                    name, user_score, computer_score, rounds
                )
                return

            else:
                print("Invalid answer! Enter yes, no, or see.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Game interrupted. Goodbye!{RESET}")
