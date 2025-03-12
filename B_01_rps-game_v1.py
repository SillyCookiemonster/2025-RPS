import random


def int_check(question, error):
    while True:

        response = input(question)

        if response == "":
            return "infinite"

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a value from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something valid
        print(error)
        print()


def instructions():
    """Prints instructions."""

    print('''***** Instructions *****

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper), or S (scissors).

The rules are as follows:
৹ Paper beats rock
৹ Rock beats scissors
৹ Scissors beats paper

Enter <xxx> to exit at anytime.

Good luck!
    ''')


def rps_compare(user, comp):
    """Compares user and computer choice"""
    if user == comp:
        return "tie"
    for i in rps_results:
        if user == i[0] and comp == i[1]:
            return i[2]


rps_list = ["rock", "paper", "scissors", "xxx"]
rps_results = [
    ("rock", "paper", "lose"),
    ("rock", "scissors", "win"),
    ("paper", "rock", "win"),
    ("paper", "scissors", "lose"),
    ("scissors", "rock", "lose"),
    ("scissors", "paper", "win"),
]
game_history = []

rounds_played = 0
mode = "regular"
rounds_won, rounds_lost, rounds_tied = 0, 0, 0

print("🪨/🗒️/✂️ Rock Paper Scissors 🪨/🗒️/✂️")

# instructions
want_instructions = string_checker("Do you want to see the instructions?  ")
if want_instructions == "yes":
    instructions()

round_num = int_check("How many rounds do you want to play?  ", "Please enter an integer that is 1 or more, or press "
                                                                "<enter> for infinite.")

if round_num == "infinite":
    mode = "infinite"

# Game loop starts here
while True:

    if rounds_played == round_num:
        break

    # Rounds headings (based on mode)
    if mode == "regular":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {round_num} 💿💿💿"
    else:
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"

    print(rounds_heading)
    print()

    # randomly choose from rps_list (excl. exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer chose:", comp_choice)

    # gets user choice
    user_choice = string_checker("Choose: ", rps_list)
    # if the user enters the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game won/lost/tied counters and add result to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔👔 It's a tie! 👔👔👔"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😢😢😢 You lose! 😢😢😢"
    else:
        rounds_won += 1
        feedback = "👍👍👍 You win! 👍👍👍"

    # setup round feedback and output to user
    # and add to game history list with round number
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback }"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

if rounds_played == 0:
    print("🐔🐔🐔 Oh no! You've chickened out! 🐔🐔🐔")
else:

    # calculate and output stats
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = rounds_tied / rounds_played * 100
    print()
    print("📊📊📊 Statistics 📊📊📊")
    print(f"Rounds won: {rounds_won} ({percent_won:.2f}%)   |   Rounds lost: {rounds_lost} ({percent_lost:.2f}%)     |   Rounds tied: {rounds_tied} ({percent_tied:.2f}%)\n")

    # asks user if they want to see history and show if yes
    see_history = string_checker("🛖🛖🛖 Do you want to see the game history 🛖🛖🛖? ")
    if see_history == "yes":
        for item in game_history:
            print(item)
