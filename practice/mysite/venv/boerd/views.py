from django.shortcuts import render
from .models import Input_Form

# Create your views here.
def input_list(request):
    lists = Input_Form.objects.all()
    return render(request,'boerd/input_list.html',{'lists':lists})