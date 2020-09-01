from django.shortcuts import render,redirect
from .forms import DocumentForm 
from .models import Document
# Create your views here.
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. This is my first Project")

def data_list(request):
    context = {'data_list': Document.objects.all()}
    return render(request , "documentary/show.html",context)

def data_form(request , id=0):
    if request.method == "GET":
        if id == 0:
            form = DocumentForm()
        else:
            dcmt = Document.objects.get(pk = id)
            form = DocumentForm(instance=dcmt)
        return render(request , "documentary/edit.html",{'form':form})
    else:
        if id == 0:
            form = DocumentForm(request.POST)
        else:
            dcmt = Document.objects.get(pk = id)
            form = DocumentForm(request.POST , instance=dcmt)

        if form.is_valid():
            form.save()
        return redirect('/Document/show')


def data_delete(request , id):
    dcmt = Document.objects.get(pk = id)
    dcmt.delete()
    return redirect('/Document/show')
    