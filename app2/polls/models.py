from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_pubished_recently(self):
        time = timezone.now()
        return time - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

    was_pubished_recently.admin_order_field = 'pub_date'
    was_pubished_recently.boolean = True
    was_pubished_recently.short_description = 'published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
