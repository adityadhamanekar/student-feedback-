from django.shortcuts import render
from feedback.models import Question
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    question1 = Question.objects.get(pk=1)  # Assuming question 1 has ID 1 in the database
    question2 = Question.objects.get(pk=2)  # Assuming question 2 has ID 2 in the database
    question3 = Question.objects.get(pk=3)  # Assuming question 3 has ID 3 in the database
    question4 = Question.objects.get(pk=4)  # Assuming question 4 has ID 4 in the database
    question5 = Question.objects.get(pk=5)  # Assuming question 5 has ID 5 in the database

    context = {
        'question1': question1,
        'question2': question2,
        'question3': question3,
        'question4': question4,
        'question5': question5,
    }
    
    return render(request, 'index.html', context)
