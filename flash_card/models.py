from django.db import models


class UploadFile(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')

class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=2000)


class Quiz(models.Model):
    quizName = models.CharField(max_length=25)
    question = models.ForeignKey(Question)

def __unicode__(self):
        return self.quizName


