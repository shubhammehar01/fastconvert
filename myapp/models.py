from django.db import models

# Create your models here.
class myUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100,default='')
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fname +" "+ self.lname
    @staticmethod
    def get_email(email):
        try:
            return myUser.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_pass(email,password):
        try:
            return myUser.objects.get(password=password,email=email)
        except:
            return False
    @staticmethod
    def get_data(email):
        try:
            return myUser.objects.get(email=email)
        except:
            return False
    
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100,default='')
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    query = models.CharField(max_length=1000)
    def __str__(self):
        return self.email

class Img(models.Model):
    img = models.ImageField()
