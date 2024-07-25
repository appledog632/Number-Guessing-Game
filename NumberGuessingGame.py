import random

# Get the number of players (1-6)
num_of_players = int(input("Enter the number of players (1-6): "))
if num_of_players <= 6:  # Ensure the number of players does not exceed 6
    # Get the start of the range for the random number
    start = int(input("Enter the start range: "))
    if start >= 0:  # Ensure the start range is not negative
        # Get the end of the range for the random number
        end = int(input("Enter the end range: "))
        if end <= 1000:  # Ensure the end range does not exceed 1000
            # Generate a random number within the specified range
            random_num = random.randint(start, end)
            z = 0  # Variable to exit the loop
            while True:  # Infinite loop for the game
                for i in range(num_of_players):  # Iterate through each player
                    # Get the guessed number from the current player
                    num_guessed = int(input('Enter the number player {}: '.format(i + 1)))
                    if num_guessed == random_num:  # Check if the guessed number is correct
                        print("Player {} won ".format(i + 1))  # Announce the winner
                        z = 1  # Set z to 1 to indicate the game is over
                        break  # Exit the loop
                    else:
                        print("Player {} your turn is over, next ".format(i + 1))  # Move to the next player
                        continue  # Continue to the next iteration of the loop
                if z == 1:  # Check if the game is over
                    break  # Exit the while loop
        else:
            print("End range must be less than or equal to 1000")
    else:
        print("Start range can't be less than zero")
else:
    print("Restart the game, number of players exceed the limit")
