from django.db import models

class Memory(models.Model):
    photo = models.ImageField(upload_to='photos/',blank=True, null=True, default='photos/AND_GATE.png')
    place = models.TextField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.place