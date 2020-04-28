from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class AnswerGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, \
                            mixins.CreateModelMixin, mixins.UpdateModelMixin, \
                            mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    lookup_field = 'id'
    
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
            return self.create(request)
    
    def put(self, request, id=None):
            return self.update(request, id)   
         
    def delete(self, request, id = None):
        return self.destroy(request, id)       



class QuestionGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, \
                            mixins.CreateModelMixin, mixins.UpdateModelMixin, \
                            mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    lookup_field = 'id'
    
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)   
         
    def delete(self, request, id = None):
        return self.destroy(request, id) 


