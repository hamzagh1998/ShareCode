from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User


def imageUploadLocation(instance, filename):
    file_path = "users/{user_id}/{user_name}-{filename}".format(user_id=instance.user.id,
                                                                user_name=instance.user.username,
                                                                filename=filename)
    return file_path

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    photo = models.ImageField(default='user_logo.png', upload_to=imageUploadLocation, blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username
