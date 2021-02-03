import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text
    
class Person(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)

#DEFAULT_PERSON_ID = 2 # For user amaghous
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text