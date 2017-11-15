from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def detail(request, question_id):
    response = "Detail page id : %s"
    return HttpResponse(response % question_id)


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