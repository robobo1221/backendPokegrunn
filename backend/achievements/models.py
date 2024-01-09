from django.db import models
from django.conf import settings
from django.core.validators import EmailValidator

class Business(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, default="", null=True, validators=[EmailValidator()])
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


ACHIEVEMENT_TYPES = (
    ("INT", "Interest"),
    ("EVENT", "Event")
)

def upload_function(instance, filename):
    pass

class Achievement(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    points = models.IntegerField(default=1, null=False)
    code = models.CharField(max_length=100, blank=False, null=False, unique=True)
    category = models.CharField(max_length=10, choices=ACHIEVEMENT_TYPES, default=ACHIEVEMENT_TYPES[0])
    image = models.ImageField(upload_to=upload_function, null=False)
    langitude = models.DecimalField(max_digits=22, decimal_places=16, null=False)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
