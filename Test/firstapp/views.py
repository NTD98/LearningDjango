from django.shortcuts import render
from firstapp.models import Topic,WebPage
# Create your views here.
def index(request):
    topic = Topic.objects.order_by('top_name')
    print(topic[0].top_name)
    my_dict={'test':topic}
    return render(request,'firstapp/index.html',context=my_dict)
