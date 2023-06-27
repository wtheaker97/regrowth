from django.shortcuts import render, redirect
from django.contrib import messages

from . import forms
from . import models

def home(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            farmer = models.Farmer.objects.get(user=user)
            farm_linkers = models.FarmFarmerLinker.objects.filter(
                farmer=farmer
            )
            farms = [fl.farm for fl in farm_linkers]
            farm_context = []
            for farm in farms:
                farm_context.append({
                    "farm": farm,
                })
            context={"farms": farm_context}
        except models.Farmer.DoesNotExist:
            context={}
        return render(request, "home.html", context)
    else:
        return redirect("accounts/login")

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
    try:
        field_links = models.FarmFieldLinker.objects.filter(
            farm=farm,
        )
        fields = [f.field for f in field_links]
    except models.FarmFieldLinker.DoesNotExist:
        fields = []
    context = {
        "farm": farm,
        "farmer": farmer,
        "started_on": started_on,
        "fields": fields
    }
    return render(request, "farm_detail.html", context)

def create_farm_field(request, farm_id):
    farm = models.Farm.objects.get(id=farm_id)
    if request.method =="POST":
        field_form = forms.FieldForm(request.POST)
        farm_linker_form = forms.FarmFieldLinkerForm(request.POST)
        if field_form.is_valid() and farm_linker_form.is_valid():
            field = field_form.save()
            farm_linker = farm_linker_form.save(commit=False)
            farm_linker.farm = farm
            farm_linker.field = field
            farm_linker.save()
            return redirect("farm_detail", farm_id=farm_id)
    else:
        field_form = forms.FieldForm()
        farm_linker_form = forms.FarmFieldLinkerForm()
        context = {
            "field_form": field_form,
            "farm_linker_form": farm_linker_form
        }
        return render(request, "create_field.html", context)
