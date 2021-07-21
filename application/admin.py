from django.contrib import admin


from .models import Bench



class BenchAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['long', 'lat', 'average_rating','nb_voters']}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
    ]

    list_display = ('long', 'lat', 'average_rating', 'nb_voters', 'date_added')
    list_filter = ['date_added', 'average_rating']

admin.site.register(Bench, BenchAdmin)