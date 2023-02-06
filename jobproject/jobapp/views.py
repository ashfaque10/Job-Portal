from django.shortcuts import render,redirect,HttpResponse
from . import forms,models
from django.core.mail import send_mail
from jobproject.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
import uuid
from django.conf import settings
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        fnm=request.POST.get('fname')
        lnm=request.POST.get('lname')
        un= request.POST.get('username')
        em=request.POST.get('email')
        pa= request.POST.get('password')
        cpa=request.POST.get('cpassword')
        if userr.objects.filter(fname=fnm):
            messages.success(request, 'first name already exist')
            return redirect(register)
        if userr.objects.filter(lname=lnm):
            messages.success(request, 'last name already exist')
            return redirect(register)
        if userr.objects.filter(username=un):
            messages.success(request, 'User name already exist')
            return redirect(register)
        if userr.objects.filter(email=em):
            messages.success(request, 'Email already exist')
            return redirect(register)
        if pa==cpa:
            b=userr(fname=fnm,lname=lnm,username=un,email=em,password=pa)
            b.save()
        a = userr.objects.filter(username=un)
        return render(request, 'uprofile.html', {'user': a})
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        un= request.POST.get('username')
        pa=request.POST.get('password')
        b = userr.objects.filter(username=un).first()
        if b is None:
            messages.success(request, 'username not found')
            return redirect(login)
        c = userr.objects.filter(password=pa).first()
        if c is None:
            messages.success(request, 'password incorrect')
            return redirect(login)
        a =userr.objects.filter(username=un)
        return render(request, 'uprofile.html', {'user': a})
    return render(request,'login.html')

def postj(request,username):
    x = User.objects.filter(username=username)
    if request.method=='POST':
        a=postjobform(request.POST)
        if a.is_valid():
            ti=a.cleaned_data['title']
            cn=a.cleaned_data['cname']
            ce=a.cleaned_data['cemail']
            exper=a.cleaned_data['expe']
            wpl=a.cleaned_data['wplace']
            em=a.cleaned_data['emp']
            a=postjob(title=ti,cname=cn,cemail=ce,expe=exper,wplace=wpl,emp=em)
            a.save()
            return HttpResponse('job posted')
        else:
            return HttpResponse('failed')
    return render(request,'postjob.html',{'x':x})

def clog(request):
    if request.method == 'POST':
        nm = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=nm).first()
        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect('/clog')
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified check your mail')
            return redirect('/clog')
        user = authenticate(username=nm, password=password)
        if user is None:
            messages.success(request, 'wrong password or email')
            return redirect('/clog')
        a=profile.objects.filter(user=user)
        return render(request,'company.html',{'company':a})
    return render(request,'clogin.html')

def creg(request):
    if request.method == 'POST':
        nm= request.POST.get('username')
        ema = request.POST.get('email')
        pa = request.POST.get('password')
        cpa=request.POST.get('cpassword')
        if User.objects.filter(username=nm).first():
            messages.success(request, 'name already exist')
            return redirect('/creg')
        if User.objects.filter(email=ema).first():
            messages.success(request, 'email already exist')
            return redirect('/creg')
        if pa==cpa:
            user_obj = User(username=nm, email=ema)
            user_obj.set_password(pa)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = profile(user=user_obj, auth_token=auth_token)
            profile_obj.save()
            sendm(ema, auth_token)
            messages.success(request, 'your registration completed check your mail')
            return redirect('/creg')
        messages.success(request,'password didnt match')
    return render(request, 'cregister.html')

def verify(request):
    return render(request,'tokensend.html')

def success(request):
    return render(request,'success.html')
def sendm(email,token):
    subject='your account has been verified'
    message=f'paste the link to verify your account http://127.0.0.1:8000/verifyy/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def verifyy(request,auth_token):
    prof_obj=profile.objects.filter(auth_token=auth_token).first()
    if prof_obj:
        if prof_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect('/clog')
        prof_obj.is_verified=True
        prof_obj.save()
        messages.success(request,'your account has been verified')
        return redirect('/clog')
    else:
        return redirect('/error')

def company(request):

    ind = User.objects.all()
    for i in ind:
        nm = i.username
        em = i.email
        id = i.id
    return render(request,'company.html',{'name':nm,'id':id,'email':em})

def error(request):
    return render(request,'error.html')

def editprofile(request,mail,token):
    if request.method == 'POST':
        a = User.objects.filter(email=mail).first()
        a.username = request.POST.get('username')
        a.email = request.POST.get('email')
        a.save()
        b = profile.objects.filter(auth_token=token)
        return render(request, 'company.html', {'company': b})
    c = profile.objects.get(auth_token=token)
    return render(request,'editp.html',{'c':c})

def rcompany(request):
    comp=User.objects.all()
    li=[]
    email=[]
    for i in comp:
        nm=i.username
        em=i.email
        li.append(nm)
        email.append(em)
        li1=li[1:]
        em1=email[1:]
    mylist=zip(li1,em1)
    return render(request,'rcompanies.html',{'mylist':mylist})


def disp(request):
    disp1=postjob.objects.all()
    return render(request,'displayj.html',{'di':disp1})

def viewp(request,id):
    view2=postjob.objects.get(id=id)
    return render(request,'viewmore.html',{'view':view2})

def userp(request):
    us=userr.objects.all()
    for i in us:
        nm=i.username
        em=i.email
        id=i.id
    return render(request,'uprofile.html',{'name':nm,'email':em,'id':id})



def userapply(request,id):
    CNM = []
    JT = []
    z = postjob.objects.get(id=id)
    cnm = z.cname
    CNM.append(cnm)
    print(CNM)
    jt = z.title
    JT.append(jt)
    mylist = zip(CNM, JT)
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        pyear = request.POST.get('passingyear')
        skills = request.POST.get('skills')
        rlocate = request.POST.get('relocate')
        pdone = request.POST.get('project')
        resume = request.FILES['resume']
        company=request.POST.get('cname')
        jobtitle=request.POST.get('jobtitle')
        b1 = applyjobmodel(fullname=fullname, phone=phone, email=email, qualification=qualification, passingyear=pyear,
                           skills=skills, relocate=rlocate, pdone=pdone, resume=resume,companyname=company,jobtitle=jobtitle)
        b1.save()
        return HttpResponse('success')
    return render(request, 'apply.html', {'company': mylist})

def view_applicants(request,username):
    CNM = []
    FNM = []
    PHN = []
    EM = []
    QL = []
    PY = []
    SK = []
    RL = []
    BE = []
    RS=[]
    JT=[]
    a=applyjobmodel.objects.filter(companyname=username)
    for i in a:
        cnm = i.companyname
        CNM.append(cnm)
        jt=i.jobtitle
        JT.append(jt)
        fnm = i.fullname
        FNM.append(fnm)
        phn = i.phone
        PHN.append(phn)
        em = i.email
        EM.append(em)
        ql = i.qualification
        QL.append(ql)
        py = i.passingyear
        PY.append(py)
        sk = i.skills
        SK.append(sk)
        rl = i.relocate
        RL.append(rl)
        be = i.pdone
        BE.append(be)
        rs = i.resume
        RS.append(str(rs).split('/')[-1])
    mylist = zip(CNM,JT, FNM, PHN, EM, QL, PY, SK, RL, BE, RS)
    return render(request,'viewa.html',{'employee':mylist})