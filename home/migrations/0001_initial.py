# Generated by Django 2.2.7 on 2020-05-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post_id', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20)),
                ('Comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('Post_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Img', models.ImageField(upload_to='')),
                ('caption', models.TextField(max_length=1000)),
                ('Username', models.CharField(max_length=20)),
                ('Likes', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_no', models.IntegerField()),
                ('Username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=20)),
                ('Bookmarks', models.TextField(max_length=10000)),
            ],
        ),
    ]
