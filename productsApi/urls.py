"""
URL configuration for productsApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import GetProducts,GetSingleProduct,GetSingleUser,GetUsers,GetUserByToken,getSellPlans
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',GetProducts),
    path('product/<int:id>',GetSingleProduct),
    path('users',GetUsers),
    path('user/<int:id>',GetSingleUser),
    path('user/getbytoken/<str:token>',GetUserByToken),
    path('sellPlans/',getSellPlans),
    path('installment',views.GetInstallMentPreview),
    path('orders/',views.getOrders),
    path('orders/<int:id>/',views.getOrderByUserId),
    path('product_installments/',views.getProductInstallment),
    path('product_installments/<int:id>/',views.getProductInstallmentByOrderId),
    path('orders_products/<int:id>/',views.getOrderProductByOrderId),
    path('companydetail/<int:id>',views.GetCompanyDetail)
]
