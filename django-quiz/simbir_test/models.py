from django.db import models


class Quiz(models.Model):
    quiz_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.quiz_text


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
