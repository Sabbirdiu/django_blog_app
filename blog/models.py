from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body =  models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail_view',args=[str(self.id)])
        
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


