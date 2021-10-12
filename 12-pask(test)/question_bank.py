class Quesetion:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



class QuestionBank:

    question_data = [
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The HTML5 standard was published in 2014.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The first computer bug was formed by faulty wires.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "Science: Computers", "type": "boolean",
            "difficulty": "medium",
            "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "medium",
            "question": "All program codes have to be compiled into an executable file in order to be run.This file can then be executed on any machine.",
                                                              "correct_answer": "False",
                                                                                "incorrect_answers": [
        "True"
    ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
                    "correct_answer": "False",
    "incorrect_answers": [
        "True"
    ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "medium", "question": "AMD created the first consumer 64-bit processor.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "'HTML' stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
                         "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "hard",
        "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8  kilobytes of memory.",
                            "correct_answer": "False",
    "incorrect_answers": [
        "True"
    ]
    }
    ]

    questions = [
        question_data("category", "correct_answer"),
    ]

    for item in question_data:
        print('question:', item[0])
        print(' correct_answer:', item[1])
        print('---')

    def run_quiz(questions):
        score = 0
        for question in questions:
            answer = input(question.questionss)
            if answer == question.answer:
                score += 1
        print("you got", score, "out of", len(questions))
    # def __init__(self, question, yes="True", no="False"):
    #     self.question = question
    #     self.yes = yes
    #     self.no = no
    #
    #
    # question_datas = [question_datas("Do you exercise?", yes=, no=0),
    #                 question_datas("Do you smoke?", yes=0, no=-10),
    #          ]


    # def __init__(self):
    #     self.question_data = [
    #             SingleGt(question="category", correct_answer="True"),
    #         ]


    # def dictionhary(self):
    #     for name in question_data:
    #         print(question_data)

    # def report(self):
    #     print(f"question: {self.question_data['question']}")
    #     print(f"correct_answer: {self.question_data['correct_answer']}")
    #
    #
    # def get_category(self):
    #     options = ""
    #     for item in self.question:
    #         options += f"{item.category}/"
    #     return options










