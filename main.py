from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_txt = q["question"]
    question_ans = q["correct_answer"]
    new_question = Question(question_txt, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_Question()

while quiz.still_has_qustion():
    quiz.next_Question()

print("You've completed the quiz")
print("Your final score was: {quiz.score}/{quiz.question_number}")
