from django.shortcuts import get_object_or_404, render

from .models import Bench
from django.utils import timezone

def index(request):
    return render(request, 'application/index.html', {})

def map(request):
    """This function displays all the benches or add a new one by POST method"""

    if request.method == 'POST':
        b = Bench(long=request.POST['long'], lat=request.POST['lat'],
                  average_rating=request.POST['vote'], nb_voters=1, date_added=timezone.now())
        b.save()
        bench_list = Bench.objects.all
        context = {'bench_list': bench_list, 'long_view': request.POST['long'], 'lat_view': request.POST['lat']}
    else:
        bench_list = Bench.objects.all

        context = {'bench_list': bench_list}
    return render(request, 'application/map.html', context)


def vote(request, bench_id):
    """This function add a vote to a bench receive by POST method and displays all the benches"""
    if request.method == 'POST':
        try:
            bench = get_object_or_404(Bench, pk=bench_id)
        except (KeyError, Bench.DoesNotExist):
            bench_list = Bench.objects.all
            context = {'bench_list': bench_list, 'error': 'An error occured !'}
            return render(request, 'application/map.html', context)
        else:
            bench.average_rating = (float(bench.average_rating * bench.nb_voters) +
                                    float(request.POST['vote'])) / (1.0 + bench.nb_voters)
            bench.nb_voters += 1
            bench.save()

            bench_list = Bench.objects.all
            context = {'bench_list': bench_list, 'long_view': bench.long, 'lat_view': bench.lat}
            return render(request, 'application/map.html', context)
    else:
        bench_list = Bench.objects.all
        context = {'bench_list': bench_list}
        return render(request, 'application/map.html', context)
