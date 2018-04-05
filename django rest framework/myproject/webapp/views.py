from django.shortcuts import render

from  django.http import HttpResponse
from django.shortcuts import  get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InformationView(APIView):

     def get(self,request):

         return Response(
             ["api/DataType/length",
             "DataType:Text or Music or Code",
             "length:Count characters"])

class TextView(APIView):
    def get(self,request,length):
        length:length
        text:["Тут должен","быть","текст от","нейронки",length]
        return Response("Нужно сгенерировать текст длиной в "+length+" символов")
class CodeView(APIView):
    def get(self,request,length):
        length:length
        text:["Тут должен","быть","код от","нейронки",length]
        return Response("Нужно сгенерировать код длиной в "+length+" символов")

