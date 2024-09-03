from django.contrib import admin
from .models import Product,User,Gender,sellPlans
from . import models
# Register your models here.



admin.site.register(Product)
admin.site.register(User)
admin.site.register(Gender)
admin.site.register(sellPlans)
admin.site.register(models.ContractInstallment)
admin.site.register(models.ContractPreRecipt)
admin.site.register(models.InstallmentPreview)
admin.site.register(models.Order)
admin.site.register(models.ProductInstallments)
admin.site.register(models.OrderProduct)
admin.site.register(models.CompanyDetail)
