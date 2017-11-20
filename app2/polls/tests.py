from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTest(TestCase):
    def test_index_view_with_future_question(self):
        create_question(question_text='Future Question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

class QuestionTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=7)
        future_question = Question(pub_date=time)

        return self.assertIs(future_question.was_pubished_recently(),False)


