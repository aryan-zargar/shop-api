from django.db import models
from uuid import uuid4
from random import randint
# Create your models here.

def generateUserCode():
    return f"sg-{randint(100000,999999)}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    Price = models.IntegerField()
    imageUrl = models.CharField(max_length = 1000000)
    desc = models.TextField(max_length=9000)
    aboutProduct = models.TextField(max_length=9000 , default="")
    def __str__(self):
        return self.name

class Gender(models.Model):
    title=models.CharField(max_length=200)

class User(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Token = models.UUIDField(null=False,default=uuid4)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    nationalCode = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    UserCode = models.CharField(max_length=200,default=generateUserCode,null=False,editable=False)


class sellPlans(models.Model):
    fromMonth = models.IntegerField()
    toMonth = models.IntegerField()
    rate = models.IntegerField(null=True)

class ContractInstallment(models.Model):
    DueDate = models.DateField(null=False)
    ContractAmount = models.IntegerField(null=False)
    ContractMainAmount = models.IntegerField(null=False)
    ContractIntrestAmount =models.IntegerField(null=False)
    ContractTotalAmount = models.IntegerField(null=False)

class ContractPreRecipt(models.Model):
    RecieptDate = models.DateField(null=False)
    PreReceiptAmount = models.IntegerField(null=False)

class InstallmentPreview(models.Model):
    FacilitiesAmount = models.IntegerField(null=False)
    FacilitiesIntrest = models.IntegerField(null=False)
    InstallmentAmount = models.IntegerField(null=False)
    LastInstallmentAmount = models.IntegerField(null=False)
    ContractPreReciptId = models.ForeignKey(ContractPreRecipt,on_delete=models.CASCADE)
    ContractInstallmentId = models.ForeignKey(ContractInstallment,on_delete=models.CASCADE)



class Order(models.Model):
    UserRef = models.ForeignKey(User,on_delete=models.CASCADE)
    Code = models.CharField(max_length=1200,null=True)
    Date = models.DateField(auto_now_add=True,null=True)
    # Code = models.IntegerField(null=True)
    IsEnded = models.BooleanField(null=True)
    def __str__(self):
        return self.Code

class ProductInstallments(models.Model):
    InstallmentIndex = models.IntegerField(null=True)
    OrderRef = models.ForeignKey(Order,on_delete=models.CASCADE)
    ProductRef = models.ForeignKey(Product,on_delete=models.CASCADE)
    Date = models.DateField()
    InstallmentPrice = models.IntegerField()
    isPayed = models.BooleanField()

class OrderProduct(models.Model):
    ProductId = models.ForeignKey(Product,on_delete=models.CASCADE)
    OrderId = models.ForeignKey(Order,on_delete=models.CASCADE)

class CompanyDetail(models.Model):
    CompanyName = models.CharField(max_length=100)
    CompanyImage = models.TextField(max_length=999999999)
    FirsPageImage = models.TextField(max_length=999999999)
    BackgroundImage = models.TextField(max_length=999999999)
