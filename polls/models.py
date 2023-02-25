from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Question(models.Model):
    question_text = models.CharField(max_length=200, default = "")
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default = None)
    choice_text = models.CharField(max_length=200, default = "")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text 

