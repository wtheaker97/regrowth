import pytest
from pytest_factoryboy import register

from tests.factories import (
    UserFactory,
    FarmFactory,
    FarmerFactory,
    FarmFarmerLinkerFactory,
    FieldFactory,
    FarmFieldLinkerFactory
)

register(UserFactory)
register(FarmFactory)
register(FarmerFactory)
register(FarmFarmerLinkerFactory)
register(FieldFactory)
register(FarmFieldLinkerFactory)

############
# Accounts #
############

@pytest.fixture
def user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def adminuser(db, user_factory):
    new_user = user_factory.create(name="admin_user", is_staff=True, is_superuser=True)
    return new_user

#########
# Farm #
#########

@pytest.fixture
def farm(db, farm_factory):
    new_farm = farm_factory.create()
    return new_farm

@pytest.fixture
def farmer(db, farmer_factory):
    new_farmer = farmer_factory.create()
    return new_farmer

@pytest.fixture
def farm_farmer_linker(db, farm_farmer_linker_factory):
    new_linker = farm_farmer_linker_factory.create()
    return new_linker

@pytest.fixture
def field(db, field_factory):
    new_field = field_factory.create()
    return new_field

@pytest.fixture
def farm_field_linker(db, farm_field_linker_factory):
    new_linker = farm_field_linker_factory.create()
    return new_linker
