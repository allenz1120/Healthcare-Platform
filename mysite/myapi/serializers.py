from rest_framework import serializers

from .models import Billing, Users, Medical_History, Role_Relation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name',
                  'date_of_birth', 'address', 'sex', 'pcp')


class BillingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Billing
        fields = ('user', 'insurance_company', 'member_id',
                  'member_name', 'credit_card', 'expiration_date', 'cvv')


class MedicalHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medical_History
        fields = ('user', 'family_predisposition', 'allergies',
                  'medication', 'drinking', 'smoking')


class RoleRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role_Relation
        fields = ('user', 'rid', 'delete',
                  'date_of_change')


# class RolesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Roles
#         fields = ('rid', 'role')
