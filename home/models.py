from django.db import models

class Users(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Phone_no=models.IntegerField()
    Username=models.CharField(max_length=20,primary_key=True)
    Password=models.CharField(max_length=20)
    Bookmarks=models.TextField(max_length=10000,default='[]')

class Posts(models.Model):
    Image=models.ImageField(upload_to='images/', default='images/None/no-image.jpg')
    caption=models.TextField(max_length=1000)
    Username=models.CharField(max_length=20)
    Likes=models.TextField(max_length=10000,default='[]')

class Comments(models.Model):
    Post_id=models.IntegerField()
    Username=models.CharField(max_length=20)
    Comment=models.TextField(max_length=500)