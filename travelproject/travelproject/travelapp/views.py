from django.http import HttpResponse
from django.shortcuts import render


def demo(request):

    return render(request, "index.html")


#def addition(request):
   # x =int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #res = x + y
    #res1 = x - y
    #res2 = x / y
    #return render(request, "result.html",{'result':res,'result1':res1,'result2':res2})



