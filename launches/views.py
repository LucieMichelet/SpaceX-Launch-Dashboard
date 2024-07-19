from django.shortcuts import render, get_object_or_404
from .models import Launch

# Create your views here.
def index(request):
    launches = Launch.objects.all()[:5]  # Limite aux 5 prochains lancements
    print(launches)
    return render(request, 'launch_index.html', {'launches': launches})

def launch_list(request):
    launches = Launch.objects.all()
    print(launches)
    return render(request, 'launch_list.html', {'launches': launches})

def launch_detail(request, launch_id):
    launch = get_object_or_404(Launch, id=launch_id)
    return render(request, 'launch_detail.html', {'launch': launch})
