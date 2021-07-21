from django.urls import path

from . import views

app_name = 'application'
urlpatterns = [
    path('', views.map, name='map'),
    path('<int:bench_id>/vote/', views.vote, name='vote'),
]
