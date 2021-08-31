from django.forms.forms import Form
from django.shortcuts import render
from demo.forms import FormPers,FormPersonne,PersonneFormset
def index(request):
    form = FormPersonne(request.POST or None)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request,'demo/home.html',context)
