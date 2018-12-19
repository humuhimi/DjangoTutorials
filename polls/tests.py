from django.test import TestCase
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
from django.urls import reverse
# Create your tests here.


def create_question(question_text,days):
    """
    今に到るまでの引数のquestion_textとdaysが含まれるもの
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    :param question_text:
    :param days:
    :return:
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        質問がなければ、おおよそのメッセージが表示される
        :return:
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'])

    def test_past_question(self):
        """
        インデックスページに過去のpub_dateを表示する
        :return:
        """
        create_question(question_text="Past question",days=-30)
        response = self.client.get(reverse('polls:index'))






class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions
        whose pub_date is in the future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for Questions
         whose pub_date is older than 1 day
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions
        whose pub_date is within the last day

        :return:
        """
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)