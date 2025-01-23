from rest_framework import serializers
from .models import Case
from accounts.models import CustomUser

class CaseSerializer(serializers.ModelSerializer):
    # Fields for related objects
    judge = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    lawyers = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')  # Automatically set, read-only

    class Meta:
        model = Case
        fields = [
            'id',
            'case_number',
            'title',
            'plaintiff',
            'defendant',
            'judge',
            'lawyers',
            'status',
            'created_by',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']  # Prevent changes to these fields

    def create(self, validated_data):
        # Remove 'lawyers' from validated_data temporarily to handle separately
        lawyers = validated_data.pop('lawyers', [])
        # Create the case instance
        case = Case.objects.create(**validated_data)
        # Set lawyers after case creation
        case.lawyers.set(lawyers)
        return case

    def update(self, instance, validated_data):
        # Remove 'lawyers' from validated_data temporarily to handle separately
        lawyers = validated_data.pop('lawyers', None)
        # Update the instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        # Update lawyers if provided
        if lawyers is not None:
            instance.lawyers.set(lawyers)
        return instance
