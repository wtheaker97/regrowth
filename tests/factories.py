import factory
from accounts.models import User
from farm.models import (
    Farm,
    Farmer,
    FarmFarmerLinker,
    Field,
    FarmFieldLinker,
)

############
# Accounts #
############

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test_user"
    email = "test@regrowth.com"
    password = "test_pass"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


########
# Farm #
########

class FarmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Farm

    name = "test_farm"
    farm_type = "self_farmed"


class FarmerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Farmer

    first_name = "Testy"
    surname = "McTester"
    user = factory.SubFactory(UserFactory)


class FarmFarmerLinkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FarmFarmerLinker

    farm = factory.SubFactory(FarmFactory)
    farmer = factory.SubFactory(FarmerFactory)
    started_on = "2000-01-01"
    stopped_on = None


class FieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Field

    name = "test_field"
    size = 20.0


class FarmFieldLinkerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FarmFieldLinker

    farm = factory.SubFactory(FarmFactory)
    field = factory.SubFactory(FieldFactory)
    acquired_on = "2000-01-01"
    removed_on = None
