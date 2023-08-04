from django.contrib.auth.decorators import login_required
import time

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PostForm
# from .forms import RegisterForm
from .models import Blog, Category, Contact, Testimonial


# @login_required(login_url='/login/')
def home(request):
    # time.sleep(2)
    posts = Blog.objects.all()
    c = Category.objects.all()
    # post = Blog.objects.filter(cat=c)
    # print(posts)
    return render(request, 'pages/home.html', {'posts': posts,'c':c})


@login_required(login_url='/login/')
def post(request, url):
    # time.sleep(3)
    p = Blog.objects.get(url=url)
    c= Category.objects.all()

    # delete code for deleting post for user
    if request.method == 'POST':
        post_id = request.POST.get('del-post-id')
        # print(post_id)
        post = Blog.objects.filter(post_id=post_id)
        post.delete()
        return redirect('/')


    # print(post)
    return render(request, 'pages/posts.html',{'p': p,'c':c})


@login_required(login_url='/login/')
def catbypost(request,url):
    cat = Category.objects.get(url=url)
    post = Blog.objects.filter(cat=cat)
    c=Category.objects.all()
    # print(c)
    return render(request, 'pages/category.html', {'ca': c, 'c': c, 'post': post})


@login_required(login_url='/login/')
def About(request):
    T = Testimonial.objects.all()
    c = Category.objects.all()
    # c = Category.objects.filter(url=Category.url)
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Message = request.POST['Message']

        contact_data = Contact.objects.create(Name=Name, Email=Email, Message=Message)

        msg = f'<script>alert("Ok {Name}, We will contact you soon :)");</script>'
        return render(request, 'pages/About.html', {'msg': msg, 'c': c, 'T': T})
    return render(request, 'pages/About.html', {'T': T, 'c': c})


def sign__up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = authenticate(username=username, password1=password1, password2=password2)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                # errors['username'] = 'This username is already taken.'
                return HttpResponse('An account with this username already exists.')
                time.sleep(2)
                return redirect('login')
            if User.objects.filter(email=email).exists():
                return HttpResponse('An account with this email already exists.')
                time.sleep(2)
                return redirect('login')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password1)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            return HttpResponse('pass dont match')

    return render(request, 'registration/sign_up.html')

    # posts section


@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


# @login_required(login_url='/login')
# def edit_post(request,url):
#     Update_data = Blog.objects.filter(post_id=id)
#     return render(request, 'update_post.html', {'Update_data': Update_data})

# @login_required(login_url='/login')
# def update_post(request,url):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('/')
#         else:
#             return HttpResponse('not working')
#     print(url)


# def update_post(request, url):
#
#     context = {}
#     # fetch the object related to passed id
#     # obj = get_object_or_404(Blog, url=url)
#     post= Blog.objects.filter(url=url)
#     # pass the object as instance in form
#     form = UpdateForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect("/blog/"+ url)
#     # add form dictionary to context
#     # context["form"] = form
#     return render(request, "posts/update_post.html",{'form':form,"post":post} )

# traditional trick
# def delete(request,url):
#     ddata = Blog.objects.get(url=url)
#     ddata.delete()
#     return redirect('/')

# class BlogUpdateview(UpdateView):
#     model=Blog
#     fields="__all__"
#     template_name='posts/update_post.html.html'
#     success_url='/'

@login_required(login_url='/login')
def edit(request, url):
    udata = Blog.objects.get(url=url)
    catdata = Category.objects.all()
    return render(request, 'posts/update_post.html', {'udata': udata, 'catdata': catdata})


@login_required(login_url='/login')
def updatefn(request, url):
    udata = Blog.objects.get(url=url)
    udata.title = request.POST['title']
    udata.content = request.POST['content']
    udata.category = request.POST['cat']
    # udata.url = request.POST['url']
    udata.image = request.FILES['img']
    # udata.update(image=image)
    # print(udata.cat)
    udata.save()
    return redirect('/')
