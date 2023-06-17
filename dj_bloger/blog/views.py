from django.shortcuts import render

from .models import Blog, Category, Contact, Testimonial


# Create your views here.
def home(request):
    # time.sleep(2)    
    posts = Blog.objects.all()
    c = Category.objects.all()
    # post = Blog.objects.filter(cat=c)
    print(posts)
    return render(request, 'pages/home.html', {'posts': posts,'c':c})


def post(request, url):
    # time.sleep(3)    
    p = Blog.objects.get(url=url)
    c= Category.objects.all()
    # print(post)
    return render(request, 'pages/posts.html',{'p': p,'c':c})

def catbypost(request,url):
    ca = Category.objects.get(url=url)
    post=Blog.objects.filter(cat=ca)
    c=Category.objects.all()
    print(c)
    return render(request,'pages/category.html', {'ca': ca,'c':c, 'post': post})


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
