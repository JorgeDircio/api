from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserMetadata(models.Model): 
    user = models.ForeignKey(User, models.DO_NOTHING)
    token = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.first_user} {self.last_name}"
    
    class Meta:
        db_table = 'user_metadata'
        verbose_name = 'User Metadata'
        verbose_name_plural = 'User Metadata'