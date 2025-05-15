from rest_framework import viewsets,permissions,status
from .serializers import TaskSerializer,TaskUpdateSerializer
from .models import Tasks
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import CustomUser



class TaskViewset(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_classes ={
        "list":TaskSerializer,
        "create":TaskSerializer,
        "retrieve":TaskSerializer,
        "update":TaskSerializer,
        "partial_update":TaskSerializer,
        "destroy":TaskSerializer,
        "mark_task_complete":TaskUpdateSerializer
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print("self",self.action)
        if self.action == "list" and self.request.user.role == CustomUser.ADMIN:
            return Tasks.objects.filter(assigned_to = self.request.user)
        return Tasks.objects.all()
    
    def get_serializer_class(self):
        return self.serializer_classes[self.action]
    
    @action(detail=True, methods=['post'])
    def mark_task_complete(self,request, pk=None):
        serializer = TaskUpdateSerializer(data=request.data)
        task = self.get_object()
        if  task.assigned_to != request.user:
            return Response({"message":"you don't have permission"},status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            task.completion_report = serializer.validated_data['completion_report']
            task.worked_hours = serializer.validated_data['worked_hours']
            task.save()
            return Response({'status': 'Task status updated'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])    
    def report(self,request, pk=None):
        task = self.get_object()
        if task.task_status != Tasks.COMPLETED:
            return Response({"message":"Task Not completed"},status=status.HTTP_200_OK)
        serializer = TaskUpdateSerializer(task,many=False)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)

        

    