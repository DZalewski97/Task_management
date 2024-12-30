from django.contrib import admin
from .models import People

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', )


# Register your models here.
