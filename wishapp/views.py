from django.shortcuts import render
from wishapp.models import Sosio_model
from django.http import HttpResponseRedirect
# Create your views here.
def display(request):
    obj = Sosio_model.objects.all()
    return render(request,'wish.html',{'obj':obj})

def wish(request):
    if request.method == "POST":
        w = request.POST['t1']
        d = request.POST['t2']
        model_obj = Sosio_model(wish=w,date=d)
        model_obj.save()
        return HttpResponseRedirect('./display')
    form = Sosio_form()
    return render(request,'wish.html',{'form':form})
