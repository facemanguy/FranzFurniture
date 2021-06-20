from django.shortcuts import get_object_or_404, render
from .models import FurnitureType, Furniture, FurnitureDetails
from django.urls import reverse_lazy
from .forms import FurnitureForm

# Create your views here.
def index (request):
    return render(request, 'franz/index.html')

def types(request):
    type_list=FurnitureType.objects.all()
    return render(request, 'franz/types.html', {'type_list' : type_list})

def getFurniture(request):
    furnList=Furniture.objects.all()
    return render(request, 'franz/furniturelist.html', {'furnList' : furnList})

def getFurnitureDetail(request, id):
    furn=get_object_or_404(Furniture, pk=id)
    deets=FurnitureDetails.objects.filter(product=id).count()
    context={
        'furn' : furn,
        'deets' : deets
    }
    return render(request, 'franz/furnituredetail.html', context=context)

def newFurniture(request):
    form=FurnitureForm

    if request.method=='POST':
        form=FurnitureForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=FurnitureForm()
    else:
        form=FurnitureForm()
    return render(request, 'franz/newfurniture.html', {'form' : form})
