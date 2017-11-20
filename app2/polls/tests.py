from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=7)
        future_question = Question(pub_date=time)

        return self.assertIs(future_question.was_pubished_recently(),False)


