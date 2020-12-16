from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.


# def index(request):
#     """
#     index  view
#     """
#     return  HttpResponse("Hello, world, You are at the polls index.")   

def index(request):
    """
    index
    """
    latest_question = Question.objects.order_by('-date_pub')[:5]
    #output = ', '.join([q.question_text for q in latest_question])
    template = loader.get_template('polls/index.html')

    context = {
        'latest_question' : latest_question,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html' , context)


def detail(request, question_id):
    """
    detail
    """
    #return HttpResponse("You are loking at %s." %question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question' : question})

def results(request, question_id):
    """
    docstring
    """
    response= "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """
    votiing
    """
    return HttpResponse("You are voting to the question %s." % question_id)


