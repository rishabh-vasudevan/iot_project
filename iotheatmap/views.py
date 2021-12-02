from django.shortcuts import render, redirect
import json
from django.conf import settings


def heatmap(request):


    return render(request, 'heatmap.html')