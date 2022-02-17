from rest_framework import serializers

from .models import Billing, Users


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
