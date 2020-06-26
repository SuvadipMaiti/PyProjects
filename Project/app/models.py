from django.db import models

# Create your models here.
class BooksNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)





class Books(models.Model):
    title = models.CharField(max_length=36, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.FloatField(default=0)
    published = models.DateField(blank=True,null=True,default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='cover/',blank=True)


    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=36)
    book = models.ForeignKey(Books,on_delete=models.CASCADE,related_name='characters')



class Author(models.Model):
    name = models.CharField(max_length=36)
    surname = models.CharField(max_length=36)
    books = models.ManyToManyField(Books,related_name='authors')



