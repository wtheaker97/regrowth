from django import forms

from . import models

class FarmForm(forms.ModelForm):
    class Meta:
        model = models.Farm
        fields = ["name", "farm_type"]


class FarmFarmerLinkerForm(forms.ModelForm):
    class Meta:
        model = models.FarmFarmerLinker
        fields = ["farmer", "started_on"]
        widgets = {
            "started_on": forms.DateInput(attrs={"type": "date"}),
        }


class FieldForm(forms.ModelForm):
    class Meta:
        model = models.Field
        fields = ["name", "size"]


class FarmFieldLinkerForm(forms.ModelForm):
    class Meta:
        model = models.FarmFieldLinker
        fields = ["acquired_on"]
        widgets = {
            "acquired_on": forms.DateInput(attrs={"type": "date"}),
        }

