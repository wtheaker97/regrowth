import pytest
from django.core.exceptions import ValidationError

def test_farm_str(farm):
    assert farm.__str__() == f"{farm.name}"

@pytest.mark.django_db
def test_farm_invalid_type(farm_factory):
    with pytest.raises(ValidationError):
        farm = farm_factory.create(farm_type="not_a_choice")

def test_farmer_name(farmer):
    assert farmer.name == f"{farmer.first_name} {farmer.surname}"

def test_farmer_str(farmer):
    assert farmer.__str__() == f"{farmer.first_name} {farmer.surname}"

def test_farm_farmer_linker_str(farm_farmer_linker):
    assert farm_farmer_linker.__str__() == f"{farm_farmer_linker.farm} - {farm_farmer_linker.farmer}"

def test_field_str(field):
    assert field.__str__() == field.name

def test_farm_field_linker_str(farm_field_linker):
    assert farm_field_linker.__str__() == f"{farm_field_linker.farm} - {farm_field_linker.field}"
