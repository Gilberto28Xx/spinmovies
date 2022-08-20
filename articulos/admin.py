from django.contrib import admin
from .models import Actors,Director,Movies,Series,Genero, Documental


# Register your models here.

class ActorsAdmin(admin.ModelAdmin):
    list_display = ("name","last_name",)

class DirectosAdmin(admin.ModelAdmin):
    list_display = ("name","last_name","movies_directed",)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ("name", "year_published","cathegory","directorf","generof",)

class DocumentalAdmin(admin.ModelAdmin):
    list_display = ("name", "year_published","cathegory","directorf","generof",)


admin.site.register(Actors, ActorsAdmin)
admin.site.register(Director, DirectosAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Series)
admin.site.register(Genero)
admin.site.register(Documental)