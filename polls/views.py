from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.http import Http404
#from django.template import loader

from .models import Question

'''
The view that manages the Urls 
'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
    #return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, 'question_id': question_id})


def results(request, question_id):
    response = "<h2>You're looking at the results of question %s.</h2>"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("<h3>You're voting on question %s.</h3>" % question_id)
