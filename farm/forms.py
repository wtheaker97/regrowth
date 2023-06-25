from django import forms

from . import models

class FarmForm(forms.ModelForm):
    class Meta:
        model = models.Farm
        fields = ["name", "farm_type"]

class FarmFarmerLinkerForm(forms.ModelForm):
    class Meta:
        model = models.FarmFarmerLinker
        fields = ["farmer"]

