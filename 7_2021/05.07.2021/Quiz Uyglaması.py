from typing import Text


class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    
    def CheckAnswer(self,answer):
        return self.answer == answer




class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def GetQuestions(self):
        return self.questions[self.question_index]

    def DisplayQuestions(self):
        question_list = self.GetQuestions()
        print(f"Soru {self.question_index + 1} : {question_list.text}")

        for q in question_list.choices:
            print("-" + q)

        answer = input(" Cevap :")
        self.Guess(answer)
        self.LoadQuestion()

    def Guess(self,answer):
        question_list = self.GetQuestions()
        if question_list.CheckAnswer(answer):
            self.score += 1
        self.question_index += 1

        

    def LoadQuestion(self):
        if len(self.questions) == self.question_index:
            self.ShowScore()
        else:
            self.DisplayProgress()
            self.DisplayQuestions()
            


    
    def ShowScore(self):
        print("Score : ",self.score)

    def DisplayProgress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number >= total_question:
            print("Quiz Bitti")

        else:
            print(f"Question : {question_number} of {total_question}".center(100,"*"))



q1 = Question("En iyi programlama dili hangisidir",
["Python","Java","Javascript","C#"],
"Python"
)
q2 = Question("En popüler programlama dili hangisidir",
["C#","Python","Java","Javascript"],
"Python"
)
q3 = Question("En çok kullanılan programlama dili hangisidir",
["Java","Javascript","Python","C#"],
"Python"
)

question_list = [q1,q2,q3]
quiz = Quiz(question_list)
question_list  = quiz.GetQuestions()

quiz.LoadQuestion()


