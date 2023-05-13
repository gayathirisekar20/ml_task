from django.shortcuts import render
import pandas as pd
from django.http import HttpResponseRedirect, HttpResponse
import csv
from .models import Cereal
from .serializers import PortSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import redirect
# Create your views here.

def load_data(request):
    # data=pd.read_csv("cereal.csv",sep=',')
    # print(data)
    

    with open('updated.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        print(data)
    return render(request,'data.html',context={"data1":data})

def add(request):
    with open('updated.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    print(data)
    # i=0
    for row in data[1:]:

        # print(i,row[9].isdigit(),row[9])
        # i=+1
        Cereal.objects.create(
            name=row[0],
            mrf=row[1],
            type=row[2],
            calories=int(row[3]),
            protein=float(row[4]),
            fat=int(row[5]),
            sodium=int(row[6]),
            fiber=float(row[7]),
            carbo=float(row[8]),
            sugars=int(row[9]),
            potass=int(row[10]),
            vitamins=int(row[11]),
            shelf=int(row[12]),
            weight=float(row[13]),
            cups=float(row[14]),
            rating=float(row[15]),
            procal=int(row[16])

        )
        response = redirect('/post/')  
    return response  
    

class Portview(ModelViewSet):
    queryset=Cereal.objects.all()
    serializer_class=PortSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type','name']
    