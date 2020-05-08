from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import  TaskForm
from django.http import HttpResponseRedirect
from .models import Task
# Create your views here.
class Home(TemplateView):
    template_name='home.html'
def home(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(redirect_to='/main')
    else:
        form=TaskForm()
    tasks=Task.objects.all()
    #print(tasks)
    context={'form':form, 'tasks':tasks}
    return render(request, 'home.html', context)
def deleteTask(request, i):
    if(request.method=='POST'):
        print(Task.objects.get(id=i))
        y = Task.objects.get(id= i)
        y.delete()
        return HttpResponseRedirect(redirect_to='/main')

