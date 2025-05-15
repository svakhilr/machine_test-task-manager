from django.db import models
from users.models import CustomUser

class Tasks(models.Model):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    
    STATUS = (
        (PENDING,"Pending"),
        (IN_PROGRESS,"In Progress"),
        (COMPLETED,"Completed"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    due_date = models.DateField()
    task_status = models.CharField(max_length=20,choices=STATUS,default=PENDING)
    completion_report = models.TextField(null=True,blank=True)
    worked_hours = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.title
