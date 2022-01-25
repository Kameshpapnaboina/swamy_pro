from django.shortcuts import render
from .models import detailmodel,exammodel
from .forms import detailform,examform
from django.contrib.auth.decorators import login_required

# Create your views here.
def one_view(request):
    form1=detailform
    if request.method=='POST':
        form1=detailform.POST
        if form1.is_valid():
            form1.save()
    return render(request,'htmlapp/one.html',{'form1':form1})
def two_view(request):
    form2=examform()
    if request.method=='POST':
        form2=examform.POST
        if form2.is_valid():
            form2.save()
        #return reidrect()
    return render(request,'htmlapp/two.html',{'form2':form2})
def three_view(request):
    return render(request,'htmlapp/three.html')
