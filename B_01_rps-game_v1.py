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


rounds_played = 0
mode = "regular"

rps_list = ["rock", "paper", "scissors", "xxx"]

print("🪨/🗒️/✂️ Rock Paper Scissors 🪨/🗒️/✂️")

# instructions
want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

round_num = int_check("How many rounds do you want to play? ", "Please enter an integer that is 1 or more, or press "
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

    # gets user choice
    user_choice = string_checker("Choose: ", rps_list)
    print(user_choice)
    # if the user enters the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

print("game finished")
