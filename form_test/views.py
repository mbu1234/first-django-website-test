from django.shortcuts import render
from . import multiplier_model as mm

def home(request):
    return render(request,'index.html')


def results(request):
    user_input = int(request.GET['user_input'])
    result = mm.multiplier(result_int)
    return render(request,'results.html',{'home_input':result})
