from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Profile
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from . serializers import ProfileSerializer


class ProfileAPIView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    lookup_field = 'id'
    def get(self, request, id=None):         
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request,id)
