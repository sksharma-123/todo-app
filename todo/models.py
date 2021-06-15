from django.db import models
import uuid


class Task(models.Model):
    curr_status = (
        ('Just_added', 'Just Added'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    task = models.CharField(max_length=100, unique=True, null=True, blank=True)
    status = models.CharField(max_length=50, choices=curr_status, default="Just Added")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.task
    