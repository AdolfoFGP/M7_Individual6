from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATE_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )

    LABEL_CHOICES = (
        ('trabajo', 'Trabajo'),
        ('hogar', 'Hogar'),
        ('estudio', 'Estudio'),
        # Agrega más etiquetas según tus necesidades
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='pendiente')
    label = models.CharField(max_length=20, choices=LABEL_CHOICES, default='trabajo')
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

