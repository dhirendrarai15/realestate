from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer,listingDetailSerializer
from datetime import datetime,timezone,timedelta

# Create your views here.

class ListingsView(ListAPIView):
    queryset = Listing.objects.order_by('-listdate').filter(ispublished = True)
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by('-listdate').filter(ispublished = True)
    serializer_class = listingDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer


    def post(self,request,format=None):
        queryset = Listing.objects.order_by('-listdate').filter(ispublished =True)
        data = self.request.data

        saletype = data['saletype']
        queryset = queryset.filter(saletype__iexact = saletype)

        price = data['price']
        if price == '$0+':
            price = 0
        elif price == '$200000+':
            price = 200000
        elif price == '$400000+':
            price = 400000
        elif price == '$600000+':
            price = 600000
        elif price == '$1000000+':
            price = 1000000
        elif price == '$1200000+':
            price = 1200000
        elif price == '$1500000+':
            price = 1500000
        elif price == 'Any':

         if price != -1:
             price = -1
        queryset = queryset.filter(price__gte=price)

        bedrooms = data['bedrooms']
        if bedrooms == '0+':
            bedrooms = 0
        elif bedrooms == '1+':
            bedrooms = 1
        elif bedrooms == '2+':
            bedrooms = 2
        elif bedrooms == '3+':
            bedrooms = 3
        elif bedrooms == '4+':
            bedrooms = 4
        elif bedrooms == '5+':
            bedrooms = 5
        queryset = queryset.filter(bedrooms__gte=bedrooms)

        hometype = data['hometype']
        queryset = queryset.filter(hometype__iexact=hometype)

        bathrooms = data['bathrooms']
        if bathrooms == '0+':
            bathrooms = 0.0
        elif bathrooms == '1+':
            bathrooms = 1.0
        elif bathrooms == '2+':
            bathrooms = 2.0
        elif bathrooms == '3+':
            bathrooms = 3.0
        elif bathrooms == '4+':
            bathrooms = 4.0

        queryset = queryset.filter(bathrooms__gte=bathrooms)

        sqft = data['sqft']
        if sqft == '1000+':
            sqft = 1000
        elif sqft == '1200+':
            sqft = 1200
        elif sqft == '1500+':
            sqft = 1500
        elif sqft == '2000+':
            sqft = 2000
        elif sqft == 'Any':
            sqft = 0

        if sqft != 0:
            queryset = queryset.filter(sqft__gte=sqft)

        dayspassed = data['dayslisted']
        if dayspassed == '1 or less':
            dayspassed = 1
        elif dayspassed == '2 or less':
            dayspassed = 2
        elif dayspassed == '5 or less':
            dayspassed = 5
        elif dayspassed == '10 or less':
            dayspassed = 10
        elif dayspassed == '20 or less':
            dayspassed = 20
        elif dayspassed == 'Any':
            dayspassed = 0

        for query in queryset:
            numdays = (datetime.now(timezone.utc) - query.listdate).days

            if dayspassed != 0:
                if numdays > dayspassed:
                    slug=query.slug
                    queryset = queryset.exclude(slug__iexact=slug)

        hasphotos = data['hasphotos']
        if hasphotos == '1+':
            hasphotos = 1
        elif hasphotos == '3+':
            hasphotos = 3
        elif hasphotos == '5+':
            hasphotos = 5
        elif hasphotos == '10+':
            hasphotos = 10
        elif hasphotos == '15+':
            hasphotos = 15

        for query in queryset:
            count = 0
            if query.photo_1:
                count += 1
            if query.photo_2:
                count += 1
            if query.photo_3:
                count += 1
            if query.photo_4:
                count += 1
            if query.photo_5:
                count += 1
            if query.photo_6:
                count += 1
            if query.photo_7:
                count += 1
            if query.photo_8:
                count += 1
            if query.photo_9:
                count += 1
            if query.photo_10:
                count += 1
            if query.photo_11:
                count += 1
            if query.photo_12:
                count += 1
            if query.photo_13:
                count += 1
            if query.photo_14:
                count += 1
            if query.photo_15:
                count += 1
            if query.photo_16:
                count += 1
            if query.photo_17:
                count += 1
            if query.photo_18:
                count += 1
            if query.photo_19:
                count += 1
            if query.photo_20:
                count += 1

            if count < hasphotos:
                slug = query.slug
                queryset = queryset.exclude(slug__iexact=slug)

        openhouse = data['openhouse']
        queryset = queryset.filter(openhouse__iexact=openhouse)

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = ListingSerializer(queryset, many=True)

        return Response(serializer.data)
