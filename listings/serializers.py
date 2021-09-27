from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'saletype', 'hometype', 'bedrooms', 'bathrooms', 'sqft', 'photomain', 'slug')

class listingDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Listing
            fields = '__all__'
            lookup_field = 'slug'