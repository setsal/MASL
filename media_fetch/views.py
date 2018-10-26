from django.shortcuts import render
from django.http import JsonResponse


from pybin.train import cluster_all as Cluster

# Create your views here.
def index(request):
    data = Cluster.getNewsCluster()
    return JsonResponse(data, safe=False)
