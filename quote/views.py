from rest_framework.views import APIView
from quote.utils.response import BaseResponse
from rest_framework.response import Response
import json
import datetime
from django.conf import settings
from quote.models import Company,User_Info
from django_redis import get_redis_connection
from django.shortcuts import HttpResponse,render,redirect
from django.core.exceptions import ObjectDoesNotExist
import redis
from quote.utils.serializer import CompanySerializer


class Company_query_list(APIView):
    '''
          retrieve:
              Return asdsadasdasdas.

          list:
              Return dasjkdlksjadkjs.

          create:
              Create a new group.

          delete:
              Remove a existing group.

          partial_update:
              Update one or more fields on a existing group.

          update:
              Update a group.
      '''
    def get(self,request):
        res = BaseResponse()
        company_list = Company.objects.all()
        ser_company_list = CompanySerializer(instance=company_list,many=True)
        print(ser_company_list)
        ret_company_list = json.dumps(ser_company_list.data, ensure_ascii=False)
        res.data = ret_company_list
        return Response(res.dict)

class Logging(APIView):
    def post(self,request):
        pass

class Regist(APIView):
    def post(self,request):
         #从request里取注册的数据
         username = request.POST['username']
         password = request.POST['password']
         User_Info.objects.create(username = username,password = password)
         return Response('ok')