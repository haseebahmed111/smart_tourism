from django import forms
from .models import *


class RecommendationForm(forms.Form):
    starting_location = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="Your City",
        widget=forms.Select(
            attrs={
                "class": "selectpicker"
            }
        ))
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label="Wants to Visit Province",
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    area = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    city = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))

    days = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    budget = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
