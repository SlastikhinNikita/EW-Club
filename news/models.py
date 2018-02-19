from django.db import models
from django.utils import timezone
# Create your models here.

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    image_field = models.ImageField(									# тоже как FileField, но с проверкой файла на "изображение"
        upload_to='uploads/%Y/%m/%d/', 
        height_field=None, 
        width_field=None, 
        max_length=100,)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    ivent_link = models.CharField(max_length=255)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
