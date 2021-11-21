from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, serializers, status
from rest_framework.response import Response 
from rest_framework.views import APIView


from appProducts.models.product import Product
from appProducts.serializers.productSerializer import ProductSerializer

class DetailProductView(generics.RetrieveAPIView):
    
    def get(self, request, pk , *args, **kwargs):
        if pk:
            queryset = Product.objects.get(pk=pk)
            serializer_class = ProductSerializer(queryset)
            
        else:
            queryset = Product.objects.all()
            serializer_class = ProductSerializer(queryset , many=True)
        return Response(serializer_class.data)
        