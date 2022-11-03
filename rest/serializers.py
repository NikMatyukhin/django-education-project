from rest_framework import serializers

from education_app.models import Work, Assessment

# Create your serializers here
class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ['name', 'description']

    # Свою валидацию можно оставить
    def validate_name(self, value):
        if 'плохое название работы' in value.lower():
            raise serializers.ValidationError('Работа не может иметь плохое название!')
        return value
    
    def validate_description(self, value):
        if len(value) == 10:
            raise serializers.ValidationError('Не круто иметь 10 символов в описании!')
        return value
