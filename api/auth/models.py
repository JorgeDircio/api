from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, name=False)
    email = models.EmailField(name=False)