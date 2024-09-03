from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product,User,sellPlans
from .serializers import productSerializer,userSerializer,sellPlanSerializer
from rest_framework.views import Response
from rest_framework import status

from . import models
from . import serializers
# Create your views here.

@api_view(['GET'])
def GetProducts(req):
    data = Product.objects.all()
    series = productSerializer(data,many=True)
    return Response(series.data)

@api_view(['GET','PUT'])
def GetSingleProduct(req,id):
    try:
        data = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response('NotFound',status=status.HTTP_404_NOT_FOUND)

    if(req.method == 'GET'):
        series = productSerializer(data)
        return Response(series.data)
    elif(req.method == 'PUT'):
        series = productSerializer(data,data=req.data)
        if series.is_valid():
            series.save()
            return Response(series.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def GetUsers(req):
    data = User.objects.all()
    series = userSerializer(data,many=True)
    return Response(series.data)

@api_view(['GET','PUT'])
def GetSingleUser(req,id):
    try:
        data = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response('NotFound',status=status.HTTP_404_NOT_FOUND)

    if(req.method == 'GET'):
        series = userSerializer(data)
        return Response(series.data)
    elif(req.method == 'PUT'):
        series = userSerializer(data,data=req.data)
        if series.is_valid():
            series.save()
            return Response(series.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def GetUserByToken(req,token):
    try:
        data = User.objects.get(Token=token)
    except User.DoesNotExist:
        return Response('NotFound',status=status.HTTP_404_NOT_FOUND)
    
    print(data)
    return Response(userSerializer(data).data)


@api_view(['GET'])
def getSellPlans(req):
    data = sellPlans.objects.all()
    series = sellPlanSerializer(data,many=True)
    return Response(series.data)



@api_view(['GET'])
def GetInstallMentPreview(req):
    InstallMentPreviewData = models.InstallmentPreview.objects.all()
    ContractPreReceipt = models.ContractPreRecipt.objects.all()
    ContractInstallment = models.ContractInstallment.objects.all()
    InstallMentPreviewDataSeries = serializers.InstallmentPreviewDTOSerializer(InstallMentPreviewData,many=True)
    ContractPreReceiptSeries = serializers.ContractPreRecieptSerializer(ContractPreReceipt,many=True)
    ContractInstallmentSeries = serializers.ContractInstallmentSerializer(ContractInstallment,many=True)
    data = {
        "InstallmentPreview":InstallMentPreviewDataSeries.data,
        "ContractPreReceipt":ContractPreReceiptSeries.data,
        "ContractInstallment":ContractInstallmentSeries.data
    }
    return Response(data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getOrders(req):
    data = models.Order.objects.all()
    series = serializers.OrderSerializer(data,many=True)
    return Response(series.data)

@api_view(['GET'])
def getOrderByUserId(req,id):
    data = models.Order.objects.filter(UserRef=id)
    series = serializers.OrderSerializer(data,many=True)
    return Response(series.data)

@api_view(['GET'])
def getProductInstallment(req):
    data = models.ProductInstallments.objects.all()
    series = serializers.ProductInstallmentSerializer(data,many=True)
    return Response(series.data)

@api_view(['GET'])
def getProductInstallmentByOrderId(req,id):
    data = models.ProductInstallments.objects.filter(OrderRef=id)
    series = serializers.ProductInstallmentSerializer(data,many=True)
    return Response(series.data)

@api_view(['GET'])
def getOrderProductByOrderId(req,id):
    data = models.OrderProduct.objects.filter(OrderId=id)
    series = serializers.OrderProductSerializer(data,many=True)
    for i in series.data:
        ProductObject = models.Product.objects.get(pk=i.get('ProductId'))
        series.data[series.data.index(i)]['imageUrl'] = serializers.productSerializer(ProductObject).data.get('imageUrl')
        series.data[series.data.index(i)]['ProductName'] = serializers.productSerializer(ProductObject).data.get('name')
    return Response(series.data)

@api_view(['GET','PUT'])
def GetCompanyDetail(req,id):
    try:
        data = models.CompanyDetail.objects.get(pk=id)
    except models.CompanyDetail.DoesNotExist:
        return Response('NotFound',status=status.HTTP_404_NOT_FOUND)

    if(req.method == 'GET'):
        series = serializers.CompanyDetailSerializer(data)
        return Response(series.data)
    elif(req.method == 'PUT'):
        series = serializers.CompanyDetailSerializer(data,data=req.data)
        if series.is_valid():
            series.save()
            return Response(series.data,status=status.HTTP_200_OK)