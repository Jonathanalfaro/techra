import datetime

from django import forms

from . import models


class CreateLocalizacion(forms.ModelForm):

    class Meta:
        model = models.Localizacion
        fields = ['latitud', 'longitud', 'user_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitud'].widget.attrs.update(
            {"type": "text", "id": "latitud", "class": "form-control", "name": "latitud", "readonly": True})
        self.fields['longitud'].widget.attrs.update(
            {"type": "text", "id": "longitud", "class": "form-control", "name": "longitud", "readonly": True})
        self.fields['user_id'].widget.attrs.update(
            {"type": "text", "id": "user_id", "class": "form-control", "name": "user_id", "readonly": True})
