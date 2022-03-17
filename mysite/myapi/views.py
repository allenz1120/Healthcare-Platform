from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer, BillingSerializer, MedicalHistorySerializer, RoleRelationSerializer, RolesSerializer
from .models import Users, Billing, Medical_History, Role_Relation, Roles


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('first_name')
    serializer_class = UserSerializer


class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all().order_by('user')
    serializer_class = BillingSerializer


class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = Medical_History.objects.all().order_by('user')
    serializer_class = MedicalHistorySerializer


class RoleRelationViewSet(viewsets.ModelViewSet):
    queryset = Role_Relation.objects.all().order_by('user')
    serializer_class = RoleRelationSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all().order_by('rid')
    serializer_class = RolesSerializer
