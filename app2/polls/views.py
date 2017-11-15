from django.http import HttpResponse
from django.shortcuts import render

def detail(request, question_id):
    response = "Detail page id : %s"
    return HttpResponse(response % question_id)


def index(request):
    return HttpResponse("<h1>Hello World!</h1>")


def result(request, question_id):
    response = "Question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vote Page: %s" % question_id)