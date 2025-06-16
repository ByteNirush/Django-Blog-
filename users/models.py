from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from pathlib import Path

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Only resize if not the default image and file exists
        if self.image and self.image.name != 'profile_pics/default.jpg':
            image_path = Path(self.image.path)
            if image_path.exists():
                img = Image.open(self.image.path)
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.image.path)