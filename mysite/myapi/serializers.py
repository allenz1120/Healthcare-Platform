from rest_framework import serializers

from .models import Users

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'date_of_birth', 'address', 'sex', 'pcp')
