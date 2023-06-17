# Generated by Django 4.2.1 on 2023-06-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_blog_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=20)),
                ('Message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='add_date',
        ),
        migrations.AddField(
            model_name='category',
            name='Add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
