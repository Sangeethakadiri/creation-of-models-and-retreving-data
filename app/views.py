from django.shortcuts import render
from django.db.models.functions import Length
from app.models import *
from django.http import HttpResponse

# Create your views here.

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',context=d)


def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.exclude(topic_name='cricket')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.filter(name__startswith='S')
    LOW=Webpage.objects.filter(name__endswith='k')
    LOW=Webpage.objects.filter(name__in=('sangeeta','karthik'))
    LOW=Webpage.objects.filter(name__contains='a')
    LOW=Webpage.objects.filter(name__regex='/w{4}')
    d={'webpage':LOW}
    return render(request,'display_webpages.html',context=d)




def update_Webpage(request):
    WOE=Webpage.objects.all()
   
    d={'Webpage':Webpage.objects.all()}
    #Webpage.objects.filter(name='').update()
    return render(request,'display_webpages.html',context=d)


def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2023-03-07')
    LOA=AccessRecord.objects.filter(date__gte='2023-03-07')
    LOA=AccessRecord.objects.filter(date__lt='2023-09-07')
    LOA=AccessRecord.objects.filter(date__lte='2023-03-07')
    LOA=AccessRecord.objects.filter(date__month='6')
    LOA=AccessRecord.objects.filter(date__year='2023')
    LOA=AccessRecord.objects.filter(date__day='23')
  

    d={'access':LOA}
    return render(request,'display_access.html',context=d)
