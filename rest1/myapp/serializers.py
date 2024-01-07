from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Person
        fields = '__all__'

    def validate(self, data):
        
        if len(data['course']) < 2 :
            raise serializers.ValidationError('Invalid Course')
        
        return data