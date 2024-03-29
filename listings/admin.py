from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ispublished', 'price', 'listdate', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('ispublished', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
