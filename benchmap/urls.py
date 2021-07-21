from django.contrib import admin
from django.urls import include, path
from application import views

urlpatterns = [
    path('application/', include('application.urls')),
    path('', views.index, name='index'),
    path('admin_content/', admin.site.urls),

]
