from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Reclamo
from .forms import ReclamoForm

# Create your views here.
def reclamo_detail(request, pk):
    reclamos = get_object_or_404(Reclamo, pk=pk)
    return render(request, 'reclamos/reclamo_detail.html', {'reclamos': reclamos})

def reclamos_list(request):
    reclamos = Reclamo.objects.all() #filter(creado__lte=timezone.now()).order_by('creado')
    return render(request, 'reclamos/reclamos_list.html', {'reclamos': reclamos})

def reclamo_new(request):
    if request.method == "POST":
        form = ReclamoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.creado = timezone.now()
            post.save()
            return redirect('reclamo_detail', pk=post.pk)
    else:
        form = ReclamoForm()
    return render(request, 'reclamos/reclamo_edit.html', {'form': form})

def reclamo_edit(request, pk):
    post = get_object_or_404(Reclamo, pk=pk)
    if request.method == "POST":
        form = ReclamoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.creado = timezone.now()
            post.save()
            return redirect('reclamo_detail', pk=post.pk)
    else:
        form = ReclamoForm(instance=post)
    return render(request, 'reclamos/reclamo_edit.html', {'form': form})