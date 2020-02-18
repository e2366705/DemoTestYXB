from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index_view(request):
    return HttpResponse('<h1><i>  直接输出  </i></h1>')


def V_web(request):
    context={
        'title': ' 跳转到 html 文件...'
    }
    return render(request , 'index.html' , context)


def one(request):
    return HttpResponse('<h1> 跳转到子路由 </h1>')


