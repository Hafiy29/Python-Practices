from Question import Question

question_prompts = [
    "What colour are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What Colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"

]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)





