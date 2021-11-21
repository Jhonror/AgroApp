from rest_framework import serializers
from appProducts.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','description','price','stock','unit_m']