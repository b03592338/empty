from django.shortcuts import render
from .models import Memory
from django.shortcuts import get_object_or_404, redirect
from .forms import Form

def base(request):
    return render(request, 'base.html')

def home(request):
    memories = Memory.objects.all()
    return render(request, 'home.html', {"memoriess" : memories})

def detail(request,memory_id):
    memories = get_object_or_404(Memory, id = memory_id)
    return render (request, 'detail.html', {'memories':memories})

def New_Memory_view(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Form()

    return render(request, 'memories_form.html', {'form':form})

def Memory_edit(request, memory_id):
    memory = get_object_or_404(Form, pk = memory_id)
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance = memory)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Form(instance = memory)

    return render(request, 'memories.html', {'form':form})