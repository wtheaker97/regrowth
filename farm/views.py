from django.shortcuts import render, redirect
from django.contrib import messages

from . import forms
from . import models

def home(request):
    user = request.user
    farmer = models.Farmer.objects.get(
        user=user
    )
    farm_linkers = models.FarmFarmerLinker.objects.filter(
        farmer=farmer
    )
    farms = [fl.farm for fl in farm_linkers]
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

def all_farms(request):
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
    return render(request, "all_farms.html", context)

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

def farm_detail(request, farm_id):
    try:
        farm = models.Farm.objects.get(id=farm_id)
    except models.Farm.DoesNotExist:
        messages.warning(request, "This farm doesn't exist.")
        return redirect("home")

    try:
        farmer_link = models.FarmFarmerLinker.objects.get(
            farm=farm,
            stopped_on=None
        )
        farmer = farmer_link.farmer
        started_on = farmer_link.started_on
    except models.FarmFarmerLinker.DoesNotExist:
        farmer = None
        started_on = None
    context = {
        "farm": farm,
        "farmer": farmer,
        "started_on": started_on
    }
    return render(request, "farm_detail.html", context)
