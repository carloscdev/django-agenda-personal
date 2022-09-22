from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    mobile = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(max_length=50)
    company = models.CharField(max_length=25)
    created = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.last_name
