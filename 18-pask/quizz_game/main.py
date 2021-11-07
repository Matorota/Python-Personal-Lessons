question_data = {
        1: {
            "question": "The HTML5 standard was published in 2014.?",
            "answer": "True"
        },
        2: {
            "question": "The first computer bug was formed by faulty wires.?",
            "answer": "False"
         },
    3: {
        "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
        "answer": "False"
    },
    4: {
        "question": "All program codes have to be compiled into an executable file in order to be run.This file can then be executed on any machine.",
        "answer": "False"
    },
    5: {
        "question": "Linus Torvalds created Linux and Git.",
        "answer": "True"
    },
    6: {
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
        "answer": "False"
    },
    7: {
        "question": "AMD created the first consumer 64-bit processor.",
        "answer": "True"
    },
    8: {
        "question": "'HTML' stands for Hypertext Markup Language.",
        "answer": "True"
    },
    9: {
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'",
        "answer": "True"
    },
    10: {
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8  kilobytes of memory.",
        "answer": "False"
    }
    }


def check_ans(question, ans, score):
    if question_data[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :(\nYour score is {score + 0}!")
        return True


def print_dictionary():
    for question_id, ques_answer in question_data.items():
        for answers in ques_answer:
            print(answers + ':', ques_answer[answers])


def info():
    print("Welcome!!!")
    print("There are a total of 10 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to start ")
    return True


intro = info()
score = 0
while True:

    for question in question_data:
        keep_going = 1
        while keep_going > 0:
            print(question_data[question]['question'])
            answer = input("Enter Answer: ")
            if answer == "skip":
                break
            check = check_ans(question, answer, score)
            if check:
                score =+ 1
                break
    break

print(f"Your final score is {score}!\n\n")

text_file = open("high_score.txt", "a")
text_file.writelines("Your total score:")
text_file.write(str(score))
text_file.writelines("\n out of 10 \n")
text_file.close()
text_file = open("high_score.txt", "r")
print(text_file.read())
text_file.close()


# b = open('high_score.txt', 'r')
#
# c = b.readlines()
# regels = len(c)
#
# print(regels)
#
# max = 0
# for line in b.readlines():
#   num = int(line.split(",")[0])
#   if (max < num > 10):
#     max = num
#
#
# print(max)
# # Close file
# b.close()



print("Thanks for playing!")