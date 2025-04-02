from django import forms

from . import models


class UpdateUsuario(forms.ModelForm):
    class Meta:
        model = models.Usuarios
        fields = ['user_techra', 'password_techra']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_techra'].widget.attrs.update(
            {"type": "text", "id": "techrausername", "class": "form-control", "name": "techrausername"})
        self.fields['password_techra'].widget.attrs.update(
            {"type": "text", "id": "techrapassword", "class": "form-control", "name": "techrapassword"})
