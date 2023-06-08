from django.db import models

class PetChoices(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    group = models.ForeignKey("groups.Group", on_delete=models.PROTECT, related_name="pets", null=True)
    sex = models.CharField(max_length=20, choices=PetChoices.choices, default=PetChoices.DEFAULT)
    traits = models.ManyToManyField("traits.trait", related_name="pets")
