from django.shortcuts import render,redirect
from .models import Users,Posts,Comments
from .forms import PostForm
from django.http import HttpResponseRedirect,HttpResponse
import json

errora=''
error=''
errorl=''
edits=''

def home(request):
    global error, errora, edits, errorl
    error=''
    edits=''
    errora=''
    errorl=''
    t=[]
    d=[]
    p=Posts.objects.all()
    if 'username' in request.session:
        u=Users.objects.get(Username=request.session['username'])
        t=json.loads(u.Likes)
        d=json.loads(u.Bookmarks)
    return render(request,'home.html',{'post':p,'likes':t,'book':d})

def signup(request):
    global errora, edits, errorl
    edits=''
    errora=''
    errorl=''
    return render(request,'signup.html',{'error':error})

def registering(request):
    firstname=request.POST.get('fname')
    lastname=request.POST.get('lname')
    phno=request.POST.get('phno')
    user=request.POST.get('username')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    for i in Users.objects.all():
        global error
        if user==i.Username:
            error='Username Already exists,Try again'
            return HttpResponseRedirect('/signup/')
    s=Users(First_Name=firstname,Last_Name=lastname,Username=user,Phone_no=phno,Email=email,Password=passw,Bookmarks='[]')
    s.save()
    request.session['name']=firstname+" "+lastname
    request.session['username']=user
    error=''
    return HttpResponseRedirect('/')

def login(request):
    global error,edits
    error=''
    edits=''
    return render(request,'login.html',{'error':errorl})

def verify(request):
    global edits
    edits=''
    user=request.POST.get('username')
    passw=request.POST.get('pass')
    for i in Users.objects.all():
        if user==i.Username and passw==i.Password:
            request.session['name']=i.First_Name+" "+i.Last_Name
            request.session['username']=i.Username
            return HttpResponseRedirect('/')
    global errorl
    errorl='Invalid username or password , Try again'
    return HttpResponseRedirect('/login/')

def viewprofile(request):
    u=Users.objects.get(Username=request.session['username'])
    return render(request,'profile.html',{'pro':u,'edits':edits})

def editprofile(request):
    global edits
    edits=''
    u=Users.objects.get(Username=request.session['username'])
    return render(request,'edit.html',{'pro':u})

def editing(request):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    c=Users.objects.get(Username=request.session['username'])
    if fname!="":
        c.First_Name=fname
    if lname!="":
        c.Last_Name=lname
    if email!="":
        c.Email=email
    if phno!="":
        c.Phone_no=phno
    c.save()
    request.session['name']=c.First_Name+" "+c.Last_Name
    global edits
    edits='Changes Successfully updated'
    return HttpResponseRedirect('/viewprofile/')

def logout(request):
    global error, errora, edits, errorl
    error=''
    edits=''
    errora=''
    errorl=''
    del request.session['username']
    del request.session['name']
    return HttpResponseRedirect('/')

def changepass(request):
    global edits
    edits=''
    return render(request,'changepass.html')

def changing(request):
    global edits
    cpass=request.POST.get('cpass')
    npass=request.POST.get('npass')
    npassa=request.POST.get('npassa')
    if npassa!=npass:
        edits='Passwords did not match'
        return HttpResponseRedirect('/viewprofile/')
    user=request.session['username']
    c=Users.objects.get(Username=user)
    if(c.Password==cpass):
        c.Password=npass
        c.save()
        edits='Password Changed Successfully'
        return HttpResponseRedirect('/viewprofile/')
    else:
        edits='Incorrect Password'
        return HttpResponseRedirect('/viewprofile/')

def myadmin(request):
    return render(request,'admin-login.html',{'error':errora})

def admin_verify(request):
    user=request.POST.get('username')
    passw=request.POST.get('pass')
    if user=='Varkha' and passw=='superuser123':
        c=Users.objects.all()
        return render(request,'admin.html',{'users':c})
    else:
        global errora
        errora='Invalid Username or Password'
        return HttpResponseRedirect('/myadmin/')

def forgotpass(request):
    return HttpResponse('Under construction')

def viewinga(request):
    user=request.POST.get('username')
    c=Users.objects.get(Username=user)
    return render(request,'profile.html',{'pro':c})

def updatinga(request):
    user=request.POST.get('username')
    c=Users.objects.get(Username=user)
    return render(request,'editadmin.html',{'pro':c})

def update(request):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    user=request.POST.get('username')
    c=Users.objects.get(Username=user)
    if fname!="":
        c.First_Name=fname
    if lname!="":
        c.Last_Name=lname
    if email!="":
        c.Email=email
    if phno!="":
        c.Phone_no=phno
    c.save()
    c=Users.objects.all()
    return render(request,'admin.html',{'users':c})

def deletinga(request):
    user=request.POST.get('username')
    Posts.objects.filter(Username=user).delete()
    Comments.objects.filter(Username=user).delete()
    Users.objects.get(Username=user).delete()
    c=Users.objects.all()
    return render(request,'admin.html',{'users':c})

def addpost(request):
    global edits
    edits=''
    return render(request,'addpost.html',context=None)

def viewposts(request):
    global edits
    edits=''
    c=Posts.objects.filter(Username=request.session['username'])
    return render(request,'viewposts.html',{'post':c})

def addingimage(request): 
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            p=Posts(Image=form.cleaned_data['image'],caption=form.cleaned_data['capt'],Likes='[]',Username=request.session['username'])
            p.save() 
            return HttpResponseRedirect('/')
    else: 
        form = PostForm() 
    return render(request, 'addpost.html', {'form' : form})

def bookmarking(request):
    if 'username' in request.session:
        u=Users.objects.get(Username=request.session['username'])
        book=json.loads(u.Bookmarks)
        pid=request.POST.get('pid')
        book.append(pid)
        u.Bookmarks=json.dumps(book)
        u.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def unbookmarking(request):
    u=Users.objects.get(Username=request.session['username'])
    book=json.loads(u.Bookmarks)
    pid=request.POST.get('pid')
    book.remove(pid)
    u.Bookmarks=json.dumps(book)
    u.save()
    return HttpResponseRedirect('/')

def liking(request):
    if 'username' in request.session:
        pid=request.POST.get('pid')
        u=Users.objects.get(Username=request.session['username'])
        p=Posts.objects.get(id=pid)
        like=json.loads(p.Likes)
        like.append(request.session['username'])
        p.Likes=json.dumps(like)
        p.save()
        like=json.loads(u.Likes)
        like.append(pid)
        u.Likes=json.dumps(like)
        u.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def unliking(request):
    pid=request.POST.get('pid')
    u=Users.objects.get(Username=request.session['username'])
    p=Posts.objects.get(id=pid)
    like=json.loads(p.Likes)
    like.remove(request.session['username'])
    p.Likes=json.dumps(like)
    p.save()
    like=json.loads(u.Likes)
    like.remove(pid)
    u.Likes=json.dumps(like)
    u.save()
    return HttpResponseRedirect('/')

def commenting(request):
    if 'username' in request.session:
        user=request.session['username']
        p=Posts.objects.get(id=request.POST.get('pid'))
        comment=request.POST.get('comment')
        c=Comments(Username=user,Comment=comment,Post_id=p.id)
        c.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def likes(request):
    postid=request.POST.get('post_id')
    l=Posts.objects.get(id=postid)
    like=json.loads(l.Likes)
    for i in like:
        try:
            user=Users.objects.get(Username=i)
            i=user.Username
        except:
            k=like.index(i)
            like[k]='Blogger'
    return render(request,'likes.html',{'likes':like})

def comments(request):
    pid=request.POST.get('pid')
    c=Comments.objects.filter(Post_id=pid)
    return render(request,'comments.html',{'com':c})

def bookmarks(request):
    global edits
    edits=''
    c=Users.objects.get(Username=request.session['username'])
    book=json.loads(c.Bookmarks)
    b=[]
    for i in book:
        try:
            b.append(Posts.objects.get(id=i))
        except:
            b.append('This post was deleted')
    return render(request,'bookmarks.html',{'book':b})

def deletepost(request):
    pid=request.POST.get('pid')
    Posts.objects.get(id=pid).delete()
    return HttpResponseRedirect('/')

def editpost(request):
    pid=request.POST.get('pid')
    c=Posts.objects.get(id=pid)
    return render(request,'editpost.html',{'post':c})

def editingpost(request):
    pid=request.POST.get('pid')
    capt=request.POST.get('capt')
    p=Posts.objects.get(id=pid)
    if capt!= '':
        p.caption=capt
        p.save()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def viewadmin(request):
    p=Posts.objects.all()
    return render(request,'adminview.html',{'post':p})

def removebookmark(request):
    p=request.POST.get('object')
    u=Users.objects.get(Username=request.session['username'])
    book=json.loads(u.Bookmarks)
    book.remove(p)
    u.Bookmarks=json.dumps(book)
    u.save()
    return HttpResponseRedirect('/')
