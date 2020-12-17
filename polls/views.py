from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.


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
    
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(date_pub__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    """
    votiing
    """
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) 
    except(KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{ 'question' : question,
        'error_message' : "You dit not select a choice" })
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


