from django.http import HttpResponse
from django.shortcuts import render
from.models import place,blog

# Create your views here.
def fun(request):
    ob = place.objects.all()
    obj = blog.objects.all()
    return render(request, "index.html", {'results': ob, 'products': obj})

def addition(request):
    num1=request.GET["num1"]
    num2 = request.GET["num2"]
    num3=num1+num2
    return render(request,'result.html',{'add':num3})