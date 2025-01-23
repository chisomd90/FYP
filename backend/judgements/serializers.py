from rest_framework import serializers
from .models import Judgement

class JudgementSerializer(serializers.ModelSerializer):
    attachments = serializers.FileField(allow_null=True, required=False)

    class Meta:
        model = Judgement
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
