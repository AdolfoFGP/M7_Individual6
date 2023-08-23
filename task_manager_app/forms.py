from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'state', 'label']


class TaskFilterForm(forms.Form):
    STATE_CHOICES = (
        ('', 'Todos'),
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )

    LABEL_CHOICES = (
        ('', 'Todas'),
        ('trabajo', 'Trabajo'),
        ('hogar', 'Hogar'),
        ('estudio', 'Estudio'),
        # Agrega más etiquetas según tus necesidades
    )

    state = forms.ChoiceField(label='Estado', choices=STATE_CHOICES, required=False)
    label = forms.ChoiceField(label='Etiqueta', choices=LABEL_CHOICES, required=False)
