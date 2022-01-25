from django import forms

from .models import ShareTrip


class ShareTripForm(forms.ModelForm):
    from_place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Starting City",
                "class": "form-control"
            }
        ))
    to_place = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Destination City",
                "class": "form-control"
            }
        ))
    vehicle = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Vehicle you used",
                "class": "form-control"
            }
        ))
    date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ))
    persons = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Total Persons on Trip",
                "class": "form-control"
            }
        ))
    budget_spent_food = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Budget Spent on Food",
                "class": "form-control"
            }
        ))
    budget_spent_hotel = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Budget Spent on Hotelling",
                "class": "form-control"
            }
        ))
    budget_spent = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Total Budget Spent",
                "class": "form-control"
            }
        ))
    heading = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Short Info",
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Describe your Trip",
                "class": "form-control"
            }
        ))
    image = forms.ImageField( required=False)

    class Meta:
        model = ShareTrip
        fields = ('from_place', 'to_place', 'vehicle','date', 'persons', 'budget_spent', 'budget_spent_food',
                  'budget_spent_hotel', 'heading', 'description', 'image')
