from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    """Abstract base model to timestamp each instance"""
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False,
        blank=False,
        help_text="Created at"
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        editable=True,
        null=True,
        blank=True,
        help_text="Modified at"
    )

    class Meta:
        abstract = True


class Farm(BaseModel):
    """Model class to store farms"""
    name = models.CharField(
        max_length=255,
        help_text="Farm name"
    )
    farm_type = models.CharField(
        max_length=32,
        choices=[
            ("self_farmed", "Self farmed"),
            ("tenented", "Tenented"),
        ],
        default="self_farmed"
    )

    def __str__(self):
        return f"{self.name}"


class Farmer(BaseModel):
    """Model class to store farmers

    Note. A farmer may or may not be linked to a user account
    """
    first_name = models.CharField(
        max_length=255,
        help_text="Farmer's first name"
    )
    surname = models.CharField(
        max_length=255,
        help_text="Farmer's surname"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="User account"
    )

    @property
    def name(self):
        """Property to store the farmer's full name"""
        return f"{self.first_name} {self.surname}"

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class FarmFarmerLinker(BaseModel):
    """Model class to link farms to farmers"""
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        blank=False
    )
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        blank=False
    )
    started_on = models.DateField(
        null=True,
        help_text="Date the farmer started farming this farm"
    )
    stopped_on = models.DateField(
        null=True,
        help_text="Date the farmer stopped farming this farm"
    )

    def __str__(self):
        return f"{self.farm} - {self.farmer}"


class Field(BaseModel):
    """Model class to store fields"""
    name = models.CharField(
        max_length=255,
        help_text="Field name"
    )
    size = models.FloatField(
        help_text="Size of field (acres)"
    )

    def __str__(self):
        return f"{self.name}"


class FarmFieldLinker(BaseModel):
    """Model class to link fields to farms"""
    farm = farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        blank=False
    )
    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        blank=False
    )
    acquired_on = models.DateField(
        help_text="Date the field was made part of the farm",
        null=True
    )
    removed_on = models.DateField(
        help_text="Date the field was removed from the farm",
        null=True
    )

    def __str__(self):
        return f"{self.farm} - {self.field}"
