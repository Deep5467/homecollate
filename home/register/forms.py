from django import forms
from .models import register_user, register_pg


class Userform(forms.ModelForm):

    class Meta:
        model = register_user
        fields = ('username', 'email', 'mobile', 'password', )

class pgform(forms.ModelForm):

    class Meta:
        model = register_pg
        fields = ('company', 'location', 'price', 'no_of_pg', )

