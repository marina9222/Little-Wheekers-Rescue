from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class GuineaPig(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(
        max_length=50,
        help_text="Name of the guinea pig"
    )
    birth_year = models.PositiveIntegerField(
        help_text="Birth year of the guinea pig"
    )
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        help_text="Image of the guinea pig"
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        help_text="Gender of the guinea pig"
    )
    adopted = models.BooleanField(
        default=False,
        help_text="Adoption status"
    )

    def __str__(self):
        return f"{self.name} ({'Adopted' if self.adopted else 'Available'})"

    @property
    def age(self):
        # Calculate age based on the birth year
        from datetime import date
        return date.today().year - self.birth_year


class Adoption(models.Model):
    guinea_pig = models.ForeignKey(
        GuineaPig,
        on_delete=models.CASCADE
    )
    adopter = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    number_of_guinea_pigs = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    living_arrangement = models.CharField(
        max_length=10,
        choices=[
            ('flat', 'Flat'),
            ('house', 'House')
        ],
        default='flat'
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Adoption of {self.guinea_pig.name} by {self.adopter.username}"
