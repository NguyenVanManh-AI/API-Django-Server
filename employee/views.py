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
