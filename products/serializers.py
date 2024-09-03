from . import models
from rest_framework.serializers import ModelSerializer

class productSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
class userSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class sellPlanSerializer(ModelSerializer):
    class Meta:
        model = models.sellPlans
        fields = '__all__'

class ContractInstallmentSerializer(ModelSerializer):
    class Meta:
        model = models.ContractInstallment
        fields= '__all__'

class ContractPreRecieptSerializer(ModelSerializer):
    class Meta:
        model = models.ContractPreRecipt
        fields= '__all__'

class InstallmentPreviewDTOSerializer(ModelSerializer):
    class Meta:
        model = models.InstallmentPreview
        fields= '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = models.Order
        fields='__all__'
class ProductInstallmentSerializer(ModelSerializer):
    class Meta:
        model = models.ProductInstallments
        fields = '__all__'
class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields = '__all__'
class CompanyDetailSerializer(ModelSerializer):
    class Meta:
        model = models.CompanyDetail
        fields = '__all__'