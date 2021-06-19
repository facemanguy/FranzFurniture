from django.shortcuts import render
from .models import FurnitureType, Furniture, FurnitureDetails

# Create your views here.
def index (request):
    return render(request, 'franz/index.html')

def types(request):
    type_list=FurnitureType.objects.all()
    return render(request, 'franz/types.html', {'type_list' : type_list})