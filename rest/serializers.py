from rest_framework import serializers
from django.contrib.auth.models import User

from education_app.models import Work, Assessment

# Create your serializers here
class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ['name', 'description']


class WorkAssessmentsSerializer(serializers.ModelSerializer):
    assessments = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='score'
    )

    class Meta:
        model = Work
        fields = ['name', 'description', 'assessments']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'is_active']
        # exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        # fields = '__all__'


class AssessmentSerializer(serializers.HyperlinkedModelSerializer):
# class AssessmentSerializer(serializers.ModelSerializer):
    # Вот так работает по умолчанию:
    # work = serializers.PrimaryKeyRelatedField(read_only=True)
    # student = serializers.PrimaryKeyRelatedField(read_only=True)
    # teacher = serializers.PrimaryKeyRelatedField(read_only=True)
    # work = serializers.StringRelatedField()
    # student = serializers.StringRelatedField()
    # teacher = serializers.StringRelatedField()
    # work = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='work-detail'
    # )
    # student = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail'
    # )
    # teacher = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail'
    # )
    # work = WorkSerializer()
    # student = UserSerializer()
    # teacher = UserSerializer()

    class Meta:
        model = Assessment
        fields = ['score', 'comment', 'work', 'student', 'teacher']
