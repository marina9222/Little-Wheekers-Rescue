from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User 

# Create your models here.

class GuineaPig(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    name = models.CharField(max_length=50, help_text="Name of the guinea pig")
    birth_year = models.PositiveIntegerField(help_text="Birth year of the guinea pig")
    image = CloudinaryField('image', blank=True, null=True, help_text="Image of the guinea pig")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text="Gender of the guinea pig")
    adopted = models.BooleanField(default=False, help_text="Adoption status")

    def __str__(self):
        return f"{self.name} ({'Adopted' if self.adopted else 'Available'})"

    @property
    def age(self):
        # Calculate age based on the birth year
        from datetime import date
        return date.today().year - self.birth_year

class Adopter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    contact_number = models.CharField(max_length=15, help_text="Adopter's contact number")
    address = models.TextField(help_text="Adopter's address")

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Adoption(models.Model):
    guinea_pig = models.ForeignKey('GuineaPig', on_delete=models.CASCADE, related_name='adoptions')
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='adoptions')
    adoption_date = models.DateField(auto_now_add=True, help_text="Date of adoption")

    def __str__(self):
        return f"{self.adopter} adopted {self.guinea_pig.name} on {self.adoption_date}"

    class Meta:
        unique_together = ('guinea_pig', 'adopter')