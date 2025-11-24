from django.db import models

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=45)
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.ip_address}"
    
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username