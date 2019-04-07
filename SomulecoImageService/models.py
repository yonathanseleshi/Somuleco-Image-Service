from django.db import models
from django.contrib.postgres.fields import ArrayField

class Image(models.Model) :
    image_id = models.UUIDField(max_length=50, unique=True, primary_key=True)
    user_id = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    s3_bucket_root_url = models.URLField(max_length=300, null=True)
    photo = models.ImageField
    type = models.CharField(max_length=30)
    upload_date = models.DateTimeField.auto_now
    tags = ArrayField(models.CharField, size=10)
    image_url = models.URLField(max_length=300)

