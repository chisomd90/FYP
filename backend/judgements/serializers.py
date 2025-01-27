from rest_framework import serializers
from .models import Judgement

class JudgementSerializer(serializers.ModelSerializer):
    attachments = serializers.FileField(allow_null=True, required=False)
    lawyer = serializers.IntegerField(source="case.lawyer.id", read_only=True)

    class Meta:
        model = Judgement
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'judge']
