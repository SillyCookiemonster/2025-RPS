def int_check(question, error):
    while True:

        response = input(question)

        if response == "":
            response = "infinite"
            return "infinite"

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


round_num = int_check("How many rounds do you want to play? ", "Please enter an integer that is 1 or more, or press "
                                                               "<enter> for infinite.")
print("Rounds to play: ", round_num)
