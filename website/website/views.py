from django.http import HttpResponse, HttpResponseRedirect   ## to give response to browser

from django.shortcuts import render, redirect
from .forms import usersForm

from service.models import Service

def homePage(request):

    servicesData =Service.objects.all()




    data={
        # 'title':'HomePage',
        # 'badata':'WElcome to my webpage',
        # 'clist':['Maths','Physics','Chemistry'],
        # 'details':[
        #             {'name':'abcd','phone':124567890},
        #             {'name':'cdef','phone': 123456}
        #             ],
        # 'numbers':[10,20,30,40,50],
        'servicesData':servicesData

    }

    return render(request,"index.html",data)

    # if request.method=="GET":
    #     output = request.GET.get('output') ##output is the key name we used earlier inside 'url' in userForm
    


    #     return render(request,"index.html",{'output':output})

def aboutUs(request):
  return HttpResponse("Welcome to my Website")

def course(request):
    return HttpResponse("<b> The course web page is under construction...</b>")

def courseDetails(request,courseid):
    return HttpResponse(courseid) 


def userForm(request):
    final_ans = 0

    fn =usersForm() 
    data = {'form':fn}

    # try: 
    #     # ONe way
    #     # n1=int(request.GET['num1'])
    #     # n2=int(request.GET['num2'])

    #     n1=int(request.GET.get('num1'))

    #     n2=int(request.GET.get('num2'))

    #     final_ans = (n1+n2)
    

    try:
        if request.method=="POST":          ##can use get also

            n1=int(request.POST.get('num1'))

            n2=int(request.POST.get('num2'))      

            final_ans =n1+n2     

            data  = {

                # 'n1':n1,
                # 'n2':n2,
                'form':fn,
                'output':final_ans,

            } 

            url = "/?output={}".format(final_ans)

            return HttpResponseRedirect(url)        ##one can also use redirect from django.shortcuts
    except:
        pass

    return render(request,'userform.html',data)


def submitform(request):
    try:
        if request.method=="POST":          ##can use get also

            n1=int(request.POST.get('num1'))

            n2=int(request.POST.get('num2'))      

            final_ans =n1+n2     

            data  = {

                'n1':n1,
                'n2':n2,
                'output':final_ans,

            } 

        return HttpResponse(final_ans)

    except:
        pass 


def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))



            operator=request.POST.get("operator")

            if operator=="+":
                c=n1+n2
            elif operator=="-":
                c=n1-n2
            elif operator=="*":
                c=n1*n2
            elif operator=="/":
                c=n1/n2
            
            #print(c,"inside try")

    except:
        c="Invalid Operation!"
    #print(c)
    return render(request, "calculator.html",{'c':c})