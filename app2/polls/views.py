from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)

    context = {
        "question" : q
    }
    return render(request, 'polls/detail.html', context)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = " //// ".join([q.question_text for q in latest_question_list])

    context = {
        "latest_question_list" : latest_question_list
    }

    return render(request,"polls/index.html",context)


def result(request, question_id):
    response = "Question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vote Page: %s" % question_id)