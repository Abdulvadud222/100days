# class UserInfo:
#
#     def __init__(self, user_id, user_name):
#         self.id = user_id
#         self.username = user_name
#         self.followers = 0
#
#
#     def add_follower(self):
#         follower_choice = input(""Type 'join' to follow: ").lower()
#         if follower_choice == "join":
#             self.followers += 1
# import random
# userid = random.randint(1, 1000)
# username = input("What is your first name: ").title()
#
# users = UserInfo(userid, username)
# users.add_follower()
# print(f"Your id is {users.id}, and your username is {users.username}. You have {users.followers} followers!")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz!\n"
      f"Your final score is: {quiz.score}/{quiz.question_number}")



