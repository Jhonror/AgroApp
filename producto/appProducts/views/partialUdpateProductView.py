from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response 
from rest_framework.views import APIView


from appProducts.models.product import Product
from appProducts.serializers.productSerializer import ProductSerializer

class PartialUdpateProductView(generics.RetrieveAPIView):
    
    def put(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(data=request.data , intance=queryset , partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data , status.HTTP_200_OK)
        return Response(serializer_class.data , status=status.HTTP_400_BAD_REQUEST)