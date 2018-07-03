from django.shortcuts import render

# Create your views here.
from fb_fetch.models import article
from fb_fetch.serializers import FB_fetchSerializer

from rest_framework import viewsets


# Create your views here.
class Fb_fetchViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = FB_fetchSerializer
