from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer, BillingSerializer
from .models import Users, Billing


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('first_name')
    serializer_class = UserSerializer


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all().order_by('user')
    serializer_class = BillingSerializer
