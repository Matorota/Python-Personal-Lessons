from single_q import question_data

print("Welcome to the game!!!\nWarning this game  insults the player constantly and its racist")
is_on = True
score = 0
while is_on:
    choice = input(f"do you wanna start the quiz or leave it Yes or No?")
    if choice == "No":
        is_on = False
    elif choice == "Yes":
        def check_ans(question, ans, attempts, score):
            if question_data[question]['answer'].lower() == ans.lower():
                print(f"Good work! \n Your score is: {score + 1}")
                return True
            else:
                print(
                    f"Wrong Answer :( \nYou have only:{attempts - 1} attemts left YOU STUPID BITCH! \nWHY YOU HAVE TO DO THIS TRY AGAIN!!!\n")
                return False
            if attempts == 0:
                print(f"you loser!!!")

        for question in question_data:
            attempts = 3
            while attempts > 0:
                print(question_data[question]['question'])
                answer = input("Enter Answer: ")
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                    attempts -= 1
    elif choice != "yes" and choice != "no":
        print("You need to wright yes or no \nYOU STUPID LEARN TO READ!!!")
        is_on = False
    elif choice == "yes" and choice == "no":
        print("Use capital letters at the beginning:D \n tu kaip nauseda.")
    else:
        print("How?!")


