from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Question

class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


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