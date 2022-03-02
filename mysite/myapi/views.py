from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer, BillingSerializer, MedicalHistorySerializer
from .models import Users, Billing, Medical_History


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('first_name')
    serializer_class = UserSerializer


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all().order_by('user')
    serializer_class = BillingSerializer


class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = Medical_History.objects.all().order_by('user')
    serializer_class = MedicalHistorySerializer
