from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from fb_fetch.models import article
from fb_fetch.serializers import FB_fetchSerializer

from rest_framework import viewsets

from pybin.train import cluster_fb

# Create your views here.
class Fb_fetchViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = FB_fetchSerializer

def index(request):
    data = cluster_fb.getCluster()

    #word = cluster_simple.getCluster()
    return JsonResponse(data, safe=False)
