from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import author, category, articale, comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import createForm,registerForm, creatrAuthor, commentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    post = articale.objects.all()
    search= request.GET.get('q')
    if search :
        post = post.filter(
            Q(title__icontains=search)|
            Q(body__icontains=search)

        )

    paginator = Paginator(post, 8) # Show 4 contacts per page
    page = request.GET.get('p')
    total_article = paginator.get_page(page)
    context= {
        "post":total_article
    }
    return render(request,"index.html",context)

def getauthor(request,name):
    post_author = get_object_or_404(User, username = name)
    auth = get_object_or_404(author, name = post_author.id)
    post =  articale.objects.filter(articale_author=auth.id)
    coantext={
        "auth":auth,
        "post":post
    }
    return render(request,"profile.html",coantext)

def getsingle(request,id):
    post = get_object_or_404(articale, pk=id)
    first = articale.objects.first()
    last = articale.objects.last()
    getcomment = comment.objects.filter(post=id)
    related = articale.objects.filter(category=post.category).exclude(id=id)[:4]
    form = commentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post=post
        instance.save()

    context={
        "post":post,
        "first": first,
        "last":last,
        "related":related,
        'form':form,
        "comment":getcomment
    }
    return render(request,"single.html",context)

# def comment_update(request):
#     post = get_object_or_404(articale, pk=id)
#     getcomment = comment.objects.filter(post=id)
#     form = commentForm(request.POST or None, instance=post)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         instance.save()
#         return redirect('index')
#     context={"form":form}
#     return render(request,"single.html",context)



def gettopic(request,name):
    cat = get_object_or_404(category,name=name)
    post = articale.objects.filter(category=cat.id)
    paginator = Paginator(post, 8) # Show 8 contacts per page

    page = request.GET.get('p')
    total_article = paginator.get_page(page)
    context = {
        "post":total_article,
        "cat":cat
    }
    return render(request,"category.html",context)

def getlogin(request):
    if request.user.is_authenticated:
       return redirect('index')
    else:
        if request.method =="POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request,username=user, password=password)
            if auth is not None:
                login(request,auth)
                return redirect('index')
            else:
                messages.add_message(request,messages.ERROR, "Username or password is not match")

    return render(request,"login.html")

def getlogout(request):
    logout(request)
    return redirect('login')

def getcreate(request):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None )
        if form.is_valid():
            instance=form.save(commit=False)
            instance.articale_author=u
            instance.save()
            return redirect('index')
        context={"form":form}
        return render(request,"create.html",context)
    else:
        return redirect('login')


def getupdate(request,id):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        post = get_object_or_404(articale,id=id)
        form = createForm(request.POST or None, request.FILES or None,instance=post )
        if form.is_valid():
            instance=form.save(commit=False)
            instance.articale_author=u
            instance.save()
            messages.success(request,"Articale is Updated successfully !")
            return redirect('profile')
        context={"form":form}
        return render(request,"create.html",context)
    else:
        return redirect('login')


def getdelete(request,id):
    if request.user.is_authenticated:
        post = get_object_or_404(articale,id=id)
        post.delete()  
        messages.warning(request,"Articale is Deleted successfully !")

        return redirect('profile')
    else:
        return redirect('login')

def getprofile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User,id=request.user.id)
        author_profle= author.objects.filter(name=user.id)
        if author_profle:
            author_user = get_object_or_404(author,name=request.user.id)
            post= articale.objects.filter(articale_author=author_user.id)
            context={
                "post":post,
                "user":author_user
            }
            return render(request,'logged_in_profile.html',context)
        else:
            form = creatrAuthor(request.POST or None, request.FILES or None )
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name=user
                instance.save()
                return redirect('profile')
            context = {
                "form":form
            }
            return render(request,"createauthor.html",context)
                
    else:
        return redirect('login')


def getregister(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()    
        messages.success(request,"Registation Successfully complate")
        return redirect('login')
    context = {
        "form":form
    }
    return render(request,"register.html",context)
