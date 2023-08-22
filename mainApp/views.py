from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from .models import Employee


# Create your views here.
def homePage(Request):
    #get all the data from database and pass as the dictinary
    data = Employee.objects.all()
    return render(Request, "index.html", {'data':data})



def add(Request):
    if(Request.method =="POST"):
        e = Employee()
        #e.name (name) will be same as the database models name.
        #POST.get("name") will be as the template name as the folder.
        e.name =  Request.POST.get("name")
        e.phone =  Request.POST.get("phone")
        e.dsg =  Request.POST.get("dsg")
        e.email =  Request.POST.get("email")
        e.salary =  Request.POST.get("salary")
        e.city =  Request.POST.get("city")
        e.state =  Request.POST.get("state")
        e.save()
        return HttpResponseRedirect("/")
    return render(Request,'add.html')



def delete(Request, id):
    try:
        data = Employee.objects.get(id=id)
        data.delete()  
    except: 
           pass   
    return HttpResponseRedirect("/")


def editrecord(Request,id):
    try:
        data = Employee.objects.get(id=id)
        if(Request.method == "POST"):
             data.name=Request.POST.get("name")
             data.email=Request.POST.get("email")
             data.phone=Request.POST.get("phone")
             data.city=Request.POST.get("city")
             data.state=Request.POST.get("state")
             data.dsg=Request.POST.get("dsg")
             data.salary=Request.POST.get("salary")
             data.save()
             return HttpResponseRedirect("/")
        return render(Request,"edit.html",{'data':data}) 
    except:         
           pass   
    return HttpResponseRedirect("/")


def searchPage(Request):
    if(Request.method=="POST"): 
         search = Request.POST.get("search")
         data = Employee.objects.filter(Q(name__icontains=search)|Q(city__icontains=search)|Q(state__icontains=search)|Q(phone__icontains=search)|Q(email__icontains=search))
         return render(Request, "index.html", {'data':data})
    else:
         return HttpResponseRedirect("/")     



