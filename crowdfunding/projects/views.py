from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import Project, Pledge, ProjectUpdates
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, ProjectUpdatesSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
# class ProjectList(generics.ListCreateAPIView):
class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    search_fields = ['title', 'description']

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data,
            status= status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        project_instance = self.get_object(pk)
        project_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PledgeList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    filterset_fields = ['anonymous','project']

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)


class ProjectUpdatesList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    queryset = ProjectUpdates.objects.all()
    serializer_class = ProjectUpdatesSerializer
    filterset_fields = ['project']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

