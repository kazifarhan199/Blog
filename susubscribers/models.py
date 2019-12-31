from django.db import models

class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        unique_together = ('email',)

    def __str__(self):
        return str(self.email)
