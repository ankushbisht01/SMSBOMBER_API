from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .smsbomber import Bomber


from . import serializers



class SendSMS(viewsets.ViewSet):
    

    serializer_class = serializers.SMSbomber

    

    def create(self, request):
        

        serializer = serializers.SMSbomber(data=request.data)

        if serializer.is_valid():
            number = serializer.data.get('number')
            no_of_sms = int(serializer.data.get('no_of_sms'))

            bomb = Bomber(number,no_of_sms)
            bomb.startBombing()           
            return Response({'message': 'Done'})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)