from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.
class GhostPost(models.Model):
    isBoast = models.BooleanField()
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now)
    secret_id = models.CharField(max_length=6)

    def __str__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        is_unique = False
        while not is_unique:
            secret_id = get_random_string(length=6)
            try:
                GhostPost.objects.get(secret_id=secret_id)
            except Exception:
                is_unique = True
        
        self.secret_id = secret_id
        return super(GhostPost, self).save(*args, **kwargs)

    @property
    def total_count(self):
        return self.upvotes - self.downvotes