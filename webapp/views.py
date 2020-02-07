from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.models import customer
from webapp.serializers import customerSerializer
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class customerList(APIView):

    def get(self, response):
        customer1 = customer.objects.all()
        serializer = customerSerializer(customer1, many=true)
        return Response(serializer.data)

    def post(self):

        pass

