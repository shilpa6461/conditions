from django.shortcuts import render

# Create your views here.

def condition1(request):
    d={'a':40}
    return render(request,'condition1.html',context=d)


def condition2(request):
    d={'a':200,'b':350}
    return render(request,'condition2.html',context=d)

def condition3(request):
    d={'a':100,'b':200,'c':400}
    return render(request,'condition3.html',context=d)
