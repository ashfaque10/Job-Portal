from django import forms

class postjobform(forms.Form):
    title=forms.CharField(max_length=20)
    cname=forms.CharField(max_length=20)
    cemail=forms.EmailField()
    expe=forms.CharField(max_length=10)
    wplace=forms.CharField(max_length=20)
    emp=forms.CharField(max_length=20)


class regform(forms.Form):
    fname=forms.CharField(max_length=20)
    lname=forms.CharField(max_length=20)
    username=forms.CharField(max_length=10)
    email=forms.EmailField()
    password=forms.CharField(max_length=10)
    cpassword=forms.CharField(max_length=10)


class logform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=10)