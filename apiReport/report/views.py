from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from report.models import Customers, Agents
from report.serializers import CustomersSerializer, AgentsSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def customers_list(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        
        customers_serializer = CustomersSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
        # 'safe=False' for objects serialization




