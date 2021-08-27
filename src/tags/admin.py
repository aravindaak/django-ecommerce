from django.contrib import admin

from .models import Tag

class TagAdmin(admin.ModelAdmin): # To show the slug as display items on admin
    list_display = ['__str__', 'slug']
    class Meta:
        model = Tag

admin.site.register(Tag)