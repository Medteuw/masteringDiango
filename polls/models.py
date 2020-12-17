from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    date_pub = models.DateTimeField('date published')

    def __str__(self):
        """
        docstring
        """
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_pub <= now
    was_published_recently.admin_order_field = 'date_pub'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        docstring
        """
        return self.choice_text
    

