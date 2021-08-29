from django.shortcuts import render, redirect
from .forms import FieldworkerForm
from .models import Fieldworker

# serialize
from rest_framework import viewsets
from .serializers import FieldworkerSerializer

# Create your views here.

# serialize
class FieldworkerViewSet(viewsets.ModelViewSet):
    queryset = Fieldworker.objects.all().order_by('first_name')
    serializer_class = FieldworkerSerializer
	
def fieldworker_list(request):
    context = {'fieldworker_list': Fieldworker.objects.all()}
    return render(request, "fieldworker_register/fieldworker_list.html", context)


def fieldworker_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FieldworkerForm()
        else:
            fieldworker = Fieldworker.objects.get(pk=id)
            form = FieldworkerForm(instance=fieldworker)
        return render(request, "fieldworker_register/fieldworker_form.html", {'form': form})
    else:
        if id == 0:
            form = FieldworkerForm(request.POST)
        else:
            fieldworker = Fieldworker.objects.get(pk=id)
            form = FieldworkerForm(request.POST,instance= fieldworker)
        if form.is_valid():
            form.save()
        return redirect('/fieldworker/list')


def fieldworker_delete(request,id):
    fieldworker = Fieldworker.objects.get(pk=id)
    fieldworker.delete()
    return redirect('/fieldworker/list')
