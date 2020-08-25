from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=99, default='Empty Search', null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search
    
    class Meta:
        verbose_name_plural = 'Searches'