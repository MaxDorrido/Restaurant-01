from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import restaurant

# Create your views here.
def index(request):
    return render(request,'index.html')
def foods(request):
    p= Paginator(restaurant.objects.all(), 9)
    if request.method == 'POST':
        food_choice=request.POST['food_choice']
        if food_choice =="all":
            p= Paginator(restaurant.objects.all(), 9)
        else:
            p= Paginator(restaurant.objects.filter(nationality=request.POST['food_choice']), 9)
    page= request.GET.get('page')
    myrestaurant= p.get_page(page)
    foodnum= "a" * myrestaurant.paginator.num_pages
    return render(request,'foods.html', {'myrestaurant':myrestaurant, 'foodnum':foodnum})
    
def sign_up(request):
    return render(request,'sign_up.html')
def sign_in(request):
    return render(request,'sign_in.html')