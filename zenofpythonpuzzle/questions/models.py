from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    p_answer1 = models.TextField()
    p_answer2 = models.TextField()
    p_answer3 = models.TextField()
    p_answer4 = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.id}.  {self.question}"