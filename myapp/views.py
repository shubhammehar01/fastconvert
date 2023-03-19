from django.shortcuts import render,HttpResponse
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Contact
from django.contrib import messages
from .models import myUser
import os
def index(request):
    if request.method=='POST':
        uploaded_file = request.FILES.getlist('img')
        choice = request.POST['select']
        print(choice)
        context = {}
        forpdf = False
        for i in uploaded_file:
            # print('value of i => ',i)
            
            file_path = default_storage.save('myapp/static/images/' + i.name, ContentFile(i.read()))
            image_path = default_storage.url(file_path)
            img = Image.open('myapp/static/images/'+i.name)
            ii = str(i)
            head,mid,tail=ii.rpartition('.')
            li = head
            flag = False
            if choice=='pdf':
                conv = img.convert('RGB')
                file = os.path.join(os.path.expanduser('~'), 'Music')
                link = os.path.join(file,li+'.pdf')     
                conv.save(link,'PDF',resolution=100.0)
                continue
            try:
                conv = img.convert('RGB')
                conv.save('myapp/static/images/converted-{l}.{ex}'.format(l=li,ex=choice),'JPEG')
            except:   
                conv = img.convert('RGBA')
                conv.save('myapp/static/images/converted-{l}.{ex}'.format(l=li,ex=choice))
            link = ''
            link += 'static/images/converted-{l}.{ex}'.format(l=li,ex=choice)
            print('this is link ',link)
            context['converted-{l}.{ex}'.format(l = li,ex=choice)]= link
        return render(request, 'index.html', {'context':context,'forpdf':forpdf,'email':request.session.get('email')})
    return render(request,'index.html',{'email':request.session.get('email')})
def about(request):
    return render(request,'about.html',{'email':request.session.get('email')})
def account(request):
    ifdata = request.session.get('email')
    if ifdata:
        data = myUser.get_data(ifdata)
        fname = ""
        lname = ""
        phone = 0
        email = ""
        if data:
            fname += data.fname        
            lname += data.lname
            phone += data.phone
            email += data.email        
        return render(request,'account.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,})
    return render(request,'signup.html')
def contact(request):
    email = request.session.get('email')
    flag = ''
    if email:
        flag += email

    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        location = request.POST['location']
        query = request.POST['textarea']
        data = Contact(fname=fname,lname=lname,phone=phone,email=email,location=location,query=query)
        data.save()
        messages.success(request,'form submitted successfully!')   
    return render(request,'contact.html',{'email':flag})
def login(request):
    if request.POST:
        email = request.POST['email']
        password =request.POST['password']

        if myUser.get_email(email)==False:
            messages.error(request,'Email not exist, check you email or create account')
            return render(request,'login.html',{'mail':email,'password':password})
        else:
            flag = myUser.get_pass(email,password)
            print(flag,password,email)
            if flag:
                messages.success(request,'login successfully !')
                request.session['email']=email
                return render(request,'index.html',{'email':request.session.get('email')})
            else:
                messages.error(request,'password didn\'t match')
                return render(request,'login.html',{'mail':email,'password':password})
    elif request.session.get('email'):
        ifdata = request.session.get('email')
        if ifdata:
            data = myUser.get_data(ifdata)
            fname = ""
            lname = ""
            phone = 0
            email = ""
            if data:
                fname += data.fname        
                lname += data.lname
                phone += data.phone
                email += data.email        
            return render(request,'account.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,})
                
    return render(request,'login.html')
def signout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request,'index.html',{'email':request.session.get('email')})
def navbar(request):
    email = request.session.get('email')
    print('navbar',email)
    if email:
        return render(request,'index.html',{'email':email})
    return render(request,'index.html')
def signup(request):
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        
        if(myUser.get_email(email=email)):
            messages.error(request,'email is already exist')
            return render(request,'signup.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        if len(password)<4:
            messages.error(request,'password must be atleast length four')
            return render(request,'signup.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        if phone.strip().isdigit()==False:
            messages.error(request,'phone number must be in digits not characters')
            return render(request,'signup.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        data = myUser(fname=fname,lname=lname,phone=phone,email=email,password=password)
        data.save()
        request.session['email']=email
        data = myUser.get_data(email)
        if data:
            request.session['fname']=data.fname
            request.session['lname']=data.lname
            request.session['phone']=data.phone
        
        messages.success(request,'Registered!')
        return render(request,'index.html',{'email':request.session.get('email')})
    elif request.session.get('email'):
        ifdata = request.session.get('email')
        if ifdata:
            data = myUser.get_data(ifdata)
            fname = ""
            lname = ""
            phone = 0
            email = ""
            if data:
                fname += data.fname        
                lname += data.lname
                phone += data.phone
                email += data.email        
            return render(request,'account.html',{'fname':fname,'lname':lname,'phone':phone,'email':email,})
                
    return render(request,'signup.html')

def sitemap(request):
    return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')
def ads(request):
    return render(request,'ads.txt')

