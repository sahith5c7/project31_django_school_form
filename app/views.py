from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *

# Create your views here.

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sl=SFDO.cleaned_data['Slocation']
            sp=SFDO.cleaned_data['Sprincipal']
            SO=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp)[0]
            SO.save()
            return HttpResponse('School is created')

    return render(request,'create_school.html',context=d)

