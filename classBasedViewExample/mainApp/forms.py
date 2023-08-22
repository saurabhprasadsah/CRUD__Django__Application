from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','phone','dsg','salary','city','state']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}),
            'dsg':forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}),
            'salary':forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'City Name'}),
            'state':forms.TextInput(attrs={'class':'form-control','placeholder':'State Name'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        dsg = self.cleaned_data['dsg']
       
        if(len(name)<3):
            raise forms.ValidationError("Invalid Name")
        if(len(email)<13):
            raise forms.ValidationError("Email Id is Not Valid")
        if(len(phone)<10):
            raise forms.ValidationError("Invalid Phone Number")
        if(len(dsg)<3):
            raise forms.ValidationError("Invalid Designation")