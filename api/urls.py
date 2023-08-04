
from django.contrib import admin
from django.urls import path, include
from api.views import CompanyVeiwSet,EmployeeVeiwSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyVeiwSet)
router.register(r'employees', EmployeeVeiwSet)
urlpatterns = [
    path('', include(router.urls))
]
