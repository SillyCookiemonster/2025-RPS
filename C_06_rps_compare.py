def rps_compare(user_choice, comp_choice):
    """Compares user and computer choice"""
    for i in to_test:
        if user_choice == i[0] and comp_choice == i[1]:
            return i[2]


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ("rock", "rock", "tie"),
    ("rock", "paper", "lose"),
    ("rock", "scissors", "win"),
    ("paper", "rock", "win"),
    ("paper", "paper", "tie"),
    ("paper", "scissors", "lose"),
    ("scissors", "rock", "lose"),
    ("scissors", "paper", "win"),
    ("scissors", "scissors", "tie"),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    user = item[0]
    comp = item[1]
    expected = item[2]

    # get actual value (ie: test ticket function)
    actual = rps_compare(user, comp)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {user} vs {comp}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {user} vs {comp}, expected: {expected}, received: {actual} ❌❌❌")
