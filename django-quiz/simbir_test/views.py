from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from simbir_test.models import *
#khlkdsghsdgvb

def index(request):
    answers = Answer.objects.get(pk=question_id)
    return render(request, 'simbir_test/index.html', {'answers': answers})


def question(request, question_id):
    questions = Question.objects.get(pk=question_id)
    answers = Answer.objects.all()
    return render(request, question_id, 'simbir_test/question.html', {'answers': answers, 'questions': questions})


def results(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)
