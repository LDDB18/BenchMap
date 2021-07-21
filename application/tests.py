from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Bench


class MapTestCase(TestCase):

    def test_add_bench(self):
        old_bench_list = Bench.objects.count()
        response = self.client.post(reverse('application:map', args=()), {
            'lat': 0.0,
            'long': 0.0,
            'vote': 2.5
        })
        new_bench_list = Bench.objects.count()  # count benches after
        self.assertEqual(new_bench_list, old_bench_list + 1)  # make sure 1 bench was added

    def test_vote(self):
        b = Bench(long=0.0, lat=0.0,
                  average_rating=2.5, nb_voters=1, date_added=timezone.now())
        b.save()
        bench_id = b.id
        response = self.client.post(reverse('application:vote', args=(bench_id, )), {
            'vote': 2.5
        })
        b_with_vote = Bench.objects.get(pk=bench_id)
        self.assertEqual(b.nb_voters + 1, b_with_vote.nb_voters)
