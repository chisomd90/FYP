from rest_framework import serializers
from .models import Document, Case, Judgement

class DocumentSerializer(serializers.ModelSerializer):
    # Link case and judgment to related fields in the serializer
    linked_case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all(), many=True, required=False)
    linked_judgment = serializers.PrimaryKeyRelatedField(queryset=Judgement.objects.all(), many=True, required=False)
    
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['uploaded_at', 'updated_at']
