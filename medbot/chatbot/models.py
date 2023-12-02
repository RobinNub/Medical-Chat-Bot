from django.db import models

class images(models.Model):
    img=models.ImageField(upload_to='chatbot/images')
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
