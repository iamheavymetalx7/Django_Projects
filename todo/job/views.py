from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

from .forms import *

##first add path in settings.py of tasks
def index(request):
    #return HttpResponse("hello world123!!")
    jobs = Job.objects.all()


    form = JobForm()

    if request.method=="POST":
        form = JobForm(request.POST)
        
        if form.is_valid:
            form.save()
        return redirect('/')

    context ={'jobs': jobs, 'form':form}

    return render(request, 'list.html',context)




def updateJob(request, pk):
    job=Job.objects.get(id=pk)

    form = JobForm(instance=job)


    if request.method=="POST":
            form = JobForm(request.POST,instance=job)

            if form.is_valid:
                form.save()
                return redirect('/')



    context = {'form' :form}

    return render(request, 'update_job.html',context)


def deleteJob(request,pk):

    item = Job.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')


    context = {'item':item}
    return render(request, 'delete.html',context)
