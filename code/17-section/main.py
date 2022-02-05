from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_object = Question(question["question"], question["correct_answer"])
    question_bank.append(q_object)

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()

print("You have completed the quiz")
print(f"Your final score is {game.score}/{game.question_number}")
