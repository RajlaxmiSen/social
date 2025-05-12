from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid
# Create your models here.

def rename_uploaded_image(filename):
    ext = filename.split('.')[-1]
    return f"profile_pics/{uuid.uuid4().hex}.{ext}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='rename_uploaded_image')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            self.image.name = rename_uploaded_image(self.image.name)
            img.save(self.image.path)

