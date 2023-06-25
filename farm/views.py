from django.shortcuts import render, redirect

from . import forms
from . import models

def home(request):
    farms = models.Farm.objects.all()
    farm_context = []
    for farm in farms:
        try:
            farmer = models.FarmFarmerLinker.objects.get(farm=farm).farmer
        except models.FarmFarmerLinker.DoesNotExist:
            farmer = None
        farm_context.append({
            "farm": farm,
            "farmer": farmer
        })
    context={"farms": farm_context}
    return render(request, "home.html", context)

def create_farm(request):
    if request.method =="POST":
        farm_form = forms.FarmForm(request.POST)
        farmer_linker_form = forms.FarmFarmerLinkerForm(request.POST)
        if farm_form.is_valid() and farmer_linker_form.is_valid():
            farm = farm_form.save()
            farmer_linker = farmer_linker_form.save(commit=False)
            farmer_linker.farm = farm
            farmer_linker.save()
            return redirect("home")
    else:
        farm_form = forms.FarmForm()
        farmer_linker_form = forms.FarmFarmerLinkerForm()
        context = {
            "farm_form": farm_form,
            "farmer_linker_form": farmer_linker_form
        }
        return render(request, "create_farm.html", context)
