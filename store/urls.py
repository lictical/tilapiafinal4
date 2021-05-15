from django.urls import path, include
from .import views#gives us access to the views


app_name = 'store'#this name has to match the one given  on the original urls.py line of code
urlpatterns = [
    path('', views.all_products, name='all_products'),#creates a path connected to the view
    #TODO: the first item is left in blank since it is rthe read director or somehting
    path('index', views.index, name='index'),
    path('check-out', views.check_out, name='check-out'),
    path('', include("django.contrib.auth.urls")),
    path('create', views.create, name="create"),

    path('login1/', views.login1, name="login1/"),
    path('logout1/', views.logout1, name="logout1/"),
]