# cars/forms.py
from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'content']


# cars/forms.py
from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'content']
