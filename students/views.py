from django.shortcuts import render
import io
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student_Admission,College
from .serializers import StudentAdmissionSerializer,studentCollegeName
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 

@csrf_exempt
def student_list(request):
  
    if request.method == 'GET':
        students = Student_Admission.objects.all()
        #college=College.objects.all()
        serializer = StudentAdmissionSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #collegedata=College.objects.get()
        data = JSONParser().parse(request)
        serializer = StudentAdmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):

    try:
        student = Student_Admission.objects.get(pk=pk)
    except student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentAdmissionSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentAdmissionSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)

def student_api(request):
    if request.method =='GET':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student_Admission.objects.get(id=id)
            serializer = StudentAdmissionSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
    
        stu= Student_Admission.object.all()
        serializer = StudentAdmissionSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')

@csrf_exempt
    
def college_details(request):
    if request.method == 'GET':
        college=College.objects.all()
        serializer1= studentCollegeName(college, many=True)
        return JsonResponse(serializer1.data, safe=False)
   
   
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer1 = studentCollegeName(data=data)
        if serializer1.is_valid():
            serializer1.save()
            return JsonResponse(serializer1.data, status=201)
        return JsonResponse(serializer1.errors, status=400)
    
    
    


     

