from django.shortcuts import render
from django.http import JsonResponse


from pybin.train import cluster_all as Cluster
import logging
import json


# Create your views here.
def index(request):
    data = Cluster.getNewsCluster()
    return JsonResponse(data, safe=False)


def customize(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)

    data = Cluster.getNewsCustomizeCluster(received_json_data['n_article'], received_json_data['month'])
    return JsonResponse(data, safe=False)
