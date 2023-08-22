from django.db.models import Q
from django.shortcuts import render,HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView,RedirectView
from django.views import View


from .forms import EmployeeForm
from .models import Employee

# class EmployeeClassView(TemplateView):
#     template_name = "index.html"
#     def get_context_data(self,*args,**kwargs):
#         context = super().get_context_data(**kwargs)
#         data = Employee.objects.all().order_by("-id")
#         return {'data':data}
    
class EmployeeClassView(View):
    def get(self,Request):
        data = Employee.objects.all().order_by("-id")
        paginator = Paginator(data, 10)
        page_number = Request.GET.get("page")
        data_obj = paginator.get_page(page_number)  
        return render(Request,"index.html",{'data':data_obj})


class EmployeePostClassView(TemplateView):
    template_name = "add.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        ef = EmployeeForm()
        context = {'form':ef}
        return context
    
    def post(self,Request):
        ef = EmployeeForm(Request.POST)
        if(ef.is_valid()):
            e = Employee()
            e.name = ef.cleaned_data['name']
            e.email = ef.cleaned_data['email']
            e.phone = ef.cleaned_data['phone']
            e.dsg = ef.cleaned_data['dsg']
            e.salary = ef.cleaned_data['salary']
            e.city = ef.cleaned_data['city']
            e.state = ef.cleaned_data['state']
            e.save()
            return HttpResponseRedirect("/")
        else:
            return render(Request,"add.html",{'form':ef})


class EmployeeDeleteView(RedirectView):
    url = "/"
    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['id']
        try:
            Employee.objects.get(id=id).delete()
        except:
            pass
        return super().get_redirect_url(*args, **kwargs)

class EmployeeUpdateClassView(View):
    template_name = "update.html"
    def get(self,Request,id):
        self.data = Employee.objects.get(id=id)
        ef = EmployeeForm(instance=self.data)
        return render(Request,"update.html",{'form':ef})
    
    def post(self,Request):
        ef = EmployeeForm(Request.POST)
        if(ef.is_valid()):
            self.data.name = ef.cleaned_data['name']
            self.data.email = ef.cleaned_data['email']
            self.data.phone = ef.cleaned_data['phone']
            self.data.dsg = ef.cleaned_data['dsg']
            self.data.salary = ef.cleaned_data['salary']
            self.data.city = ef.cleaned_data['city']
            self.data.state = ef.cleaned_data['state']
            self.data.save()
            return HttpResponseRedirect("/")
        else:
            return render(Request,"add.html",{'form':ef})

class EmployeeSearchView(View):
    def post(self,Request):
        if(Request.method=="POST"):
            search = Request.POST.get('search')
            data = Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(phone__icontains=search)|Q(dsg__icontains=search)|Q(city__icontains=search)|Q(state__icontains=search))
            paginator = Paginator(data, 10)
            page_number = Request.GET.get("page")
            data_obj = paginator.get_page(page_number)  
            return render(Request,"index.html",{'data':data_obj})
        else:
            return HttpResponseRedirect("/")




# def homePage(Request):
#     data = Employee.objects.all().order_by("-id")
#     paginator = Paginator(data, 1)
#     page_number = Request.GET.get("page")
#     data_obj = paginator.get_page(page_number)
#     return render(Request,"index.html",{"data":data_obj})

# def addPage(Request):
#     if(Request.method=="POST"):
#         ef = EmployeeForm(Request.POST)
#         if(ef.is_valid()):
#             e = Employee()
#             e.name = ef.cleaned_data['name']
#             e.email = ef.cleaned_data['email']
#             e.phone = ef.cleaned_data['phone']
#             e.dsg = ef.cleaned_data['dsg']
#             e.salary = ef.cleaned_data['salary']
#             e.city = ef.cleaned_data['city']
#             e.state = ef.cleaned_data['state']
#             e.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(Request,"add.html",{'form':ef})
#     else:
#         ef = EmployeeForm()
#         return render(Request,"add.html",{'form':ef})


# def deletePage(Request,id):
#     try:
#         data = Employee.objects.get(id=id).delete()
#     except:
#         pass
#     return HttpResponseRedirect("/")


# def updatePage(Request,id):
#     try:
#         data = Employee.objects.get(id=id)
#         if(Request.method=="POST"):
#             ef = EmployeeForm(Request.POST)
#             if(ef.is_valid()):
#                 data.name = ef.cleaned_data['name']
#                 data.email = ef.cleaned_data['email']
#                 data.phone = ef.cleaned_data['phone']
#                 data.dsg = ef.cleaned_data['dsg']
#                 data.salary = ef.cleaned_data['salary']
#                 data.city = ef.cleaned_data['city']
#                 data.state = ef.cleaned_data['state']
#                 data.save()
#                 return HttpResponseRedirect("/")
#         else:
#             ef = EmployeeForm(instance=data)
#             return render(Request,"update.html",{'form':ef})
#     except:
#         pass
#     return HttpResponseRedirect("/")


# def searchPage(Request):
#     if(Request.method=="POST"):
#         search = Request.POST.get('search')
#         data = Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(phone__icontains=search)|Q(dsg__icontains=search)|Q(city__icontains=search)|Q(state__icontains=search))
#         return render(Request,"index.html",{'data':data})
#     else:
#         return HttpResponseRedirect("/")