from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Question

'''
def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)

    context = {
        "question" : q
    }
    return render(request, 'polls/detail.html', context)
'''

class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = " //// ".join([q.question_text for q in latest_question_list])

    context = {
        "latest_question_list" : latest_question_list
    }

    return render(request,"polls/index.html",context)
'''
'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})
'''

class ResultView(DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,"polls/detail.html",{
        'question' : question,
        'error_message' : "You didn't select a choice."
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', pk=pk)