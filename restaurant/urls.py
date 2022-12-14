from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foods', views.foods, name='foods'),
    path('signup', views.sign_up, name='sign_up'),
    path('signin', views.sign_in, name='sign_in'),
]