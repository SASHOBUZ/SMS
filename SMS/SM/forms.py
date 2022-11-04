from django.forms import ModelForm
from .models import *


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class FeesForm(ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'
