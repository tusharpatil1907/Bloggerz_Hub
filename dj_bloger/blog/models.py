from django.db import models
from django.utils.html import format_html
# from tinymce.models import HTMLField


# Create your models here.
# category model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    Add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    # to display image in admin panel
    def image_tag(self):
        return format_html('<img height="60" width="60" style="border-radius:40px" src="/media/{}">'.format(self.image))


# post models

class Blog(models.Model):

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    ##content = HTMLField()
    content = models.TextField(max_length=10000)
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/")
    add_date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html(f'<img style="height:50px;width:50px; border-radius:40px" src="/media/{self.image}">')

    def title_tag(self):
        return format_html(f'<p>{self.title}</p>')


class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Message = models.TextField(max_length=1000)
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name

    def title_tag(self):
        return format_html(f'<h6>{self.Name}</h6>')


CHOICES = (
    ("Full Stack Developer", "Full Stack Developer"),
    ("Backend Developer", "Backend Developer"),
    ("Frontend Developer", "Frontend Developer"),
    ("Manager", "Manager"),
    ("Tester", "Tester"),
    ("Intern", "Intern"),
)


class Testimonial(models.Model):
    Name = models.CharField(max_length=50)
    Role = models.CharField(max_length=20, choices=CHOICES)
    Message = models.TextField(max_length=1000)
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name

    def title_tag(self):
        return format_html(f'<h5>{self.Name}</h5>')