from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questions = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    questions.append(new_question)

quiz = QuizBrain(questions)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()

print("You have finished the Quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")