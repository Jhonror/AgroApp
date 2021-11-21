from rest_framework import status, views
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response 
from rest_framework.views import APIView

from appProducts.serializers.productSerializer import ProductSerializer

class ProductCreateView(views.APIView):
    
    def post(self, request, *args, **kwargs):        
        serializer_class = ProductSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data , status=status.HTTP_201_CREATED)
        return Response(serializer_class.data , status=status.HTTP_400_BAD_REQUEST)
    
