from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from affairs.models import Student
from myapiapp.serializers import UserSerializer, GroupSerializer, StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# to handle the student viewset => view the
class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('student_id')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def update_student(request, pk):
    student = Student.objects.get(student_id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_student(request, pk):
    student = Student.objects.get(student_id=pk)
    student.delete()
    return Response("Deleted Successfully")
