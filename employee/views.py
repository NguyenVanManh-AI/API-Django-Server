from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single employee
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    # delete a single employee
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single employee
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_employee(request):
    # get all employee
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    # insert a new record for a employee
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age'))
        }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# up file
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

# cũ 
# def upload(request):
#     if request.method == 'POST' and request.FILES['file']:
#         # Lưu file vào server
#         file = request.FILES['file']
#         fs = FileSystemStorage()
#         filename = fs.save(file.name, file)

#         # Trả về thông tin về file đã lưu
#         return JsonResponse({'filename': filename})
#     else:
#         return JsonResponse({'error': 'Invalid request'})
    
# upload 1 file  
# upfile  

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileUploadSerializer

# class FileUploadView(APIView):
#     def post(self, request):
#         serializer = FileUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             file = serializer.validated_data['file']
#             # Xử lý file tại đây
#             fs = FileSystemStorage()
#             filename = fs.save(file.name, file)
#             return JsonResponse({'filename': filename})
#         else:
#             return Response(serializer.errors, status=400)
# upfile 
# upload 1 file  

# upload nhiều file 
import os
import shutil
import json 
from rest_framework.parsers import MultiPartParser

from unidecode import unidecode # xóa dấu trong python 
def handle_uploaded_file(file,user_id,user_fullname):
    fs = FileSystemStorage()
    user_fullname = unidecode(user_fullname).replace(" ", "-")
    fs.save(user_id+'-'+user_fullname+'-'+file.name, file)
    # path = '/avatar/'
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # with open(os.path.join(path, file.name), 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            user_data = json.loads(request.data['user']) # dưới client là chuyển object thành string 
            # lên đây chuyển string về lại json 
            user_id = user_data.get('id')
            user_fullname = user_data.get('fullname')
            for file in serializer.validated_data['files']:
                handle_uploaded_file(file,user_id,user_fullname)
            return Response({'status': 'OK'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# upload nhiều file 
