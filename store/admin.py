from django.contrib import admin
from .models import Category, Product, Kassenzettel# we use the . operator to not confuse the folders
#TODO: investigate when to use the ".xxxx" when doing a from ".models import"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):#there are several parametres that can be used. check documentation
    #TODO: CHECK THE ADMIN SERIES TO FIGURE OUT ALL YOU CAN DO WITH THE ADMIN FUNCTIONS ON YOUTUBE
    list_display = ['name', 'slug']# this is a parameter that belongs to admin and i will display this parameters on the list that is all
    prepopulated_fields =  {'slug': ('name',)}#the prepopulated field will make that when i write the name field on the database then the slug will be the same


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']#creates a filter to show
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Kassenzettel)
class CategoryAdmin(admin.ModelAdmin):#there are several parametres that can be used. check documentation
    #TODO: CHECK THE ADMIN SERIES TO FIGURE OUT ALL YOU CAN DO WITH THE ADMIN FUNCTIONS ON YOUTUBE
    list_display = ['name', 'price']# this is a parameter that belongs to admin and i will display this parameters on the list that is all
    #prepopulated_fields =  {'slug': ('name',)}#the prepopulated field will make that when i write the name field on the database then the slug will be the same
