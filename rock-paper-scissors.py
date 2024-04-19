import random

choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice in choices:
        computer_choice = random.choice(choices)
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break
    else:
        print("Invalid choice! Please enter rock, paper, or scissors.")
