# from django.forms import ModelForm
# from .models import Room
#
# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'

from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
