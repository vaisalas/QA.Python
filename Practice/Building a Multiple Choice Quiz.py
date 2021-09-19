from Question import Question

questions = [
    Question (question_prompts [0], "a"),
    Question (question_prompts [1], "c"),
    Question (question_prompts [2], "b"),]

def run_test(questions):
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct") 

run_test(questions)
