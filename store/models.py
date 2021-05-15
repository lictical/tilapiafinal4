from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):#create database for a category table of products
    name = models.CharField(max_length=255, db_index=True)#
    slug = models.SlugField(max_length=255, unique=True)#this refers to the name required to access the product in the database in the www.myhshop,com/shop/SLUG

    class Meta: # create more instructions by overriding this class in django
        verbose_name_plural = 'categories'

    # def get_absolut_url(self):#TODO: will also be explain later on the video
    #     return reversed('store:category_list', args= [self.slug])

    def __str__(self):
        #TODO: define later in the video first introduce in 18:39
        return self.name

class Product(models.Model):# create a database that refers to the specific prodcut
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)#creates a foreign key that is a link to the category table
    #TODO: FINDOUT WHWAT IS A FOREIGNKEY IN SQL AND HOW IT RELATES TWO DATABASE TABLES introduced in min 19:52
    #"""on_delete=models.CASCADE""" assures that if the father table of category is errased so will the products that are under them.
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_create')# just makes a connection to who create this table
    ###1. lets create book type products
    title = models.CharField(max_length=255)#row of the table
    author = models.CharField(max_length=255, default='admin')#row of the table
    description = models.TextField(blank=True)#TextField allos more text than Charfield

    image = models.ImageField(upload_to='images/')#we do not save the img on database instead only the link
    #TODO: LATER ON CREATE A DATDABASE TABLE SPECIFICALLY FOR image introduce in 24:22
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)#maybe your product is in stock but you are not selling
    created = models.DateTimeField(auto_now_add= True)# this stores the date when was created
    updated = models.DateTimeField(auto_now= True)# this stores the data when it was updated


    class Meta:#overriding one of the classess from inheritance models.Model
        verbose_name_plural = 'Products'#just changes the name
        ordering = ('-created',)# it orders your data in the way you want- on this case it orders on descending order from "Created"

    def __str__(self):
        return self.title




class Kassenzettel(models.Model):# lets create a model for our shopping list
    kassenzettel = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE)#this model is related to each user
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kassenzettel_create')

    #lets create the elements of our model
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:#overriding one of the classess from inheritance models.Model
        verbose_name_plural = 'Kassenzettel'#just changes the name
        #ordering = ('-created',)# it orders your data in the way you want- on this case it orders on descending order from "Created"

    def __str__(self):
        return self.name



