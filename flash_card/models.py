from django.db import models

# Would it be worth tying this UploadFile model to the Question/Quiz it's tied to
class UploadFile(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')

class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)

# I'm guessing that Quiz will be tied to many Questions so that you can make a deck of questions?
class Quiz(models.Model):
    quizName = models.CharField(max_length=25)
    # You'll just need to change this relationship to ManytoMany
    question = models.ForeignKey(Question)

def __unicode__(self):
        return self.quizName


