from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     content = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(content,request))
#
#
# def detail(request,question_id):
#     '''
#        it can use shortcut get_object_or_404
#         try:
#            question = Question.objects.get(pk=question_id)
#        except Question.DoesNotExist:
#            raise Http404("Question does not exist")
#        :param request:
#        :param question_id:
#        :return:
#     '''
#
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#
# def vote(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError,Choice.DoesNotExist): # 投票フォームの再表示
#         return render(request,'polls/detail.html', {
#             'question':question,
#             'error_message':"Choiceを選んでください",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# try generic views

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """最後に発行されたquestionsを返す"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):  # same with no generic here
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist): # 投票フォームの再表示
        return render(request,'polls/detail.html', {
            'question':question,
            'error_message':"Choiceを選んでください",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))











