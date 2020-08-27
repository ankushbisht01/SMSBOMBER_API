from rest_framework import serializers
from django.core.validators import RegexValidator , MaxValueValidator



class SMSbomber(serializers.Serializer):
    number = serializers.CharField(max_length = 10,validators=[RegexValidator(r'^\d\d\d\d\d\d\d\d\d\d{1,10}$')] )
    no_of_sms = serializers.CharField(max_length=3,validators=[RegexValidator(r'^(\d\d)?\d{1,10}$')])