from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from django.template import loader

from django import forms


from .models import Question, Choice, Person

'''
The view that manages the Urls 
'''

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
    #return HttpResponse(output)

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, 'question_id': question_id})

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    choice_list = []
    for choice in choices:
        choice_list.append([choice.choice_text, choice.votes])
        #choice_vote_list.append(choice.votes)
    context = {
        'question_text': question.question_text,
        'choice_list': choice_list,
        #'choice_text_list': choice_text_list,
        #'choice_vote_list': choice_vote_list,
    }

    return render(request, 'polls/results.html', context)

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ['username', 'phone_number']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(user.password) # set password properly before commit
        if commit:
            user.save()
        return user

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('polls:login')
    template_name = 'registration/signup.html'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

def user_login(request): # each request is related to it's own user
    if request.method == 'POST':
        try:        
            username = request.POST['username']
            password = request.POST['password']
            if Person.objects.filter(username=username).exists():
                user = Person.objects.get(username=username)
                if user.check_password(password):
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('home')
                else:
                    print("Password check failed")
            else:
                return redirect('polls:login')
        except Exception as problem:
            print(problem)
            return redirect('polls:login')
    return render(request, 'polls/login.html')

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:3]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
