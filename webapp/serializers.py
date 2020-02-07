from rest_framework import serializers
from webapp.models import customer

class customerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        fields = ('first_name', 'second_name', 'number', 'location')
        # fields ='__all__'

