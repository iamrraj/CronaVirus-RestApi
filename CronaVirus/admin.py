from django.contrib import admin
from .models import CronaVirus, Area, Cities, News, Remours
# Register your models here.


class CronaAdmin(admin.ModelAdmin):
    list_display = ["pk", 'currentConfirmedCount', 'confirmCount', 'suspectedCount',
                    'curedCount', 'deadCount', 'seriousCount', 'currentConfirmedIncr']


class AreaAdmin(admin.ModelAdmin):
    list_display = ['pk', 'continentName', 'country', 'locationId', 'currentConfirmedCount',
                    'confirmCount', 'suspectedCount', 'curedCount', 'deadCount']
    search_fields = ['country', 'continentName', 'locationId',
                     'currentConfirmedCount', 'deadCount']


class CitiesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cityName', 'locationId', 'currentConfirmedCount',
                    'confirmCount', 'suspectedCount', 'curedCount', 'deadCount']
    search_fields = ['cityName',
                     'currentConfirmedCount', 'deadCount', 'locationId', 'suspectedCount']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'provinceId', 'provinceName', 'pubdate']
    ordering = ['pk']


class ResmouAdmin(admin.ModelAdmin):
    list_display = ['pk', '_id', 'title']
    ordering = ['pk']


admin.site.register(CronaVirus, CronaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Remours, ResmouAdmin)
