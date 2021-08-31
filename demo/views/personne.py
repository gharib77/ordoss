from django.shortcuts import render
from demo.models.personne import Personne
from django.http import HttpResponse
def list_pers(request):
    records=Personne.objects.all()
    context={'records':records}
    return render(request,'demo/personnes/list_pers.html',context)