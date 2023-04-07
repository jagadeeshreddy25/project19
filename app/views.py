from django.shortcuts import render
from app.models import*
# Create your views here.
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'Topic':LOT}
    return render(request,'display_Topic.html',context=d)
def display_Webpage(request):
    LOW=Webpage.objects.all()
   LOW=Webpage.objects.filter(topic_name='cricket')
    d={'Webpage':LOW}
    return render(request,'display_Webpage.html',context=d)
def display_Acessrecord(request):
    LOA=Acessrecord.objects.all()
    d={'Acessrecord':LOA}
    return render(request,'display_Acessrecord.html',d)