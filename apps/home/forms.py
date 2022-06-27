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


class CustomTripOfferForm(forms.ModelForm):
    trip_from = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="Your City",
        widget=forms.Select(
            attrs={
                "class": "selectpicker"
            }
        ))
    to_province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        label="Province to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    to_area = forms.ModelChoiceField(
        queryset=Area.objects.all(),
        label="Area to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="City to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    destination_note = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    max_budget = forms.IntegerField(
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
    min_days = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    max_days = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = CustomTripOffer
        fields = ['trip_from', 'to_province', 'to_area', 'to_city', 'destination_note', 'max_budget', 'persons',
                  'min_days', 'max_days', 'description']


class CustomTripOfferViewForm(forms.ModelForm):
    trip_from = forms.ModelChoiceField(
        disabled=True,
        queryset=City.objects.all(),
        label="Your City",
        widget=forms.Select(
            attrs={
                "class": "selectpicker"
            }
        ))
    to_province = forms.ModelChoiceField(
        disabled=True,

        queryset=Province.objects.all(),
        label="Province to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    to_area = forms.ModelChoiceField(
        disabled=True,

        queryset=Area.objects.all(),
        label="Area to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    to_city = forms.ModelChoiceField(
        disabled=True,

        queryset=City.objects.all(),
        label="City to visit",
        required=False,
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    destination_note = forms.CharField(
        disabled=True,

        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    max_budget = forms.IntegerField(
        disabled=True,

        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    persons = forms.IntegerField(
        disabled=True,

        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    min_days = forms.IntegerField(
        disabled=True,

        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    max_days = forms.IntegerField(
        disabled=True,

        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    description = forms.CharField(
        disabled=True,

        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = CustomTripOffer
        fields = ['trip_from', 'to_province', 'to_area', 'to_city', 'destination_note', 'max_budget', 'persons',
                  'min_days', 'max_days', 'description']


class CustomTripOfferBidForm(forms.ModelForm):
    trip_from = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="Your City",
        widget=forms.Select(
            attrs={
                "class": "selectpicker"
            }
        ))

    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="City to visit",
        widget=forms.Select(
            attrs={
                "class": "selectpicker"

            }
        ))
    budget = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    persons = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    days = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = CustomTripBid
        fields = ['trip_from', 'to_city',  'budget', 'persons','days', 'description']
