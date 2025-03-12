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


print("🪨/🗒️/✂️ Rock Paper Scissors 🪨/🗒️/✂️")

rounds_played = 0
mode = "regular"
round_num = int_check("How many rounds do you want to play? ", "Please enter an integer that is 1 or more, or press "
                                                               "<enter> for infinite.")

if round_num == "infinite":
    mode = "infinite"

# Game looop starts here
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
    user_choice = input("Choose: ")

    # if the user enters the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

print("game finished")
