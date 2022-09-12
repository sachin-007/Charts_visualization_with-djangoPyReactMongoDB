from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from assignment.models import jsondatas
from assignment.serializers import AssignmentSerializer
 
# Create your views here.

@csrf_exempt
def assignmentApi(request,id=0):
    if request.method=='GET':
        Jsondatas=jsondatas.objects.all()
        Assignment_Serializer=AssignmentSerializer(Jsondatas,many=True)
        return JsonResponse(Assignment_Serializer.data,safe=False)
    elif request.method=='POST':
        Jsondata_data=JSONParser().parse(request)
        Assignment_Serializer=AssignmentSerializer(data=Jsondata_data)
        if Assignment_Serializer.is_valid():
            Assignment_Serializer.save()
            return JsonResponse("Added successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    