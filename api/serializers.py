# this file we're going to need to create model serializers because the response object cannot natively handle complex data types such as django model instances so we'll first need to serialize this data before we can actually render it out so we'll create serializers for our item  model and all this will do is convert instances of our items from objects into data types the response object can understand
from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'