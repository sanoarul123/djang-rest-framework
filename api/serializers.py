from rest_framework import serializers
from students.models import student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"