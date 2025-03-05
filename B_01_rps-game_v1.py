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


print("💎/🗒️/✂️ Rock Paper Scissors 💎/🗒️/✂️")

rounds_played = 0
mode = "regular"
round_num = int_check("How many rounds do you want to play? ", "Please enter an integer that is 1 or more, or press "
                                                               "<enter> for infinite.")
print("Rounds to play: ", round_num)

if round_num == "infinite":
    mode = "infinite"

while True:

    if rounds_played == round_num:
        break

    if mode == "regular":
        print("Round number:", (rounds_played - round_num) * -1)
        rounds_played += 1
    else:
        rounds_played += 1
        print("Round number:", rounds_played)

    user_choice = input("Choose: ")
    if user_choice == "xxx":
        break


print("game finished")
