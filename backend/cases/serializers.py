from rest_framework import serializers
from .models import Case
from accounts.models import CustomUser

class CaseSerializer(serializers.ModelSerializer):
    # Fields for related objects
    judge = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    # Lawyer field as a ForeignKey, make it optional
    lawyer = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='LAWYER'),
        required=False  # Make lawyer optional
    )
    
    # Automatically set 'created_by' to the username, read-only
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Case
        fields = [
            'id',
            'case_number',
            'title',
            'plaintiff',
            'defendant',
            'judge',
            'lawyer',  # Single lawyer (foreign key)
            'status',
            'created_by',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        print(f"Creating case with data: {validated_data}")  # Debugging log
        return Case.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

