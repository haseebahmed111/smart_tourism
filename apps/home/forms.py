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
        label="Province to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    area = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        label="Area to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="City to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))

    days = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    budget = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    persons = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
