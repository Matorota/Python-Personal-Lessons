def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer


question_prompts = [
    "The HTML5 standard was published in 2014?\n(a) true \n(b) false\n\n",
    "The first computer bug was formed by faulty wires?\n(a) true \n(b) false\n\n",
    "FLAC stands for 'Free Lossless Audio Condenser?\n(a) true \n(b) false\n\n",
    "Linus Torvalds created Linux and Git?\n(a) true \n(b) false\n\n",
    "AMD created the first consumer 64-bit processor?\n(a) true \n(b) false\n\n",
    "HTML stands for Hypertext Markup Language?\n(a) true \n(b) false\n\n",
    "All program codes have to be compiled into an executable file in order to be run. This file can then be executed "
    "on any machine.?\n(a) true \n(b) false\n\n",
    "The programming language Python is based off a modified version of JavaScript?\n(a) true \n(b) false\n\n",
    "In most programming languages, the operator ++ is equivalent to the statement '+= 1'?\n(a) true \n(b) false\n\n",
    "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory?\n(a) true \n(b) "
    "false\n\n",
    "All program codes have to be compiled into an executable file in order to be run. This file can then be executed "
    "on any machine?\n(a) true \n(b) false\n\n",

]

questions = [
    question_prompts[0], "a",
    question_prompts[1], "b",
    question_prompts[2], "b",
    question_prompts[3], "a",
    question_prompts[4], "a",
    question_prompts[5], "b",
    question_prompts[6], "b",
    question_prompts[7], "a",
    question_prompts[8], "b",
    question_prompts[9], "b"
]


def run_test(questions1):
    score = 0
    for question in questions1:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions1)) + " correct")


run_test(questions)
