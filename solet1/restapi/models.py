from django.db import models
from django.core.validators import ValidationError


# Create your models here.
def validateCategory(value):
    if value != "persuasive" and value != "summary":
        raise ValidationError("Not a valid category")


class Metric(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, validators=[validateCategory])

    def __str__(self):
        return self.title


class Prompt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, validators=[validateCategory])

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Rubric(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, validators=[validateCategory])

    def __str__(self):
        return self.title


class MentorText(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, validators=[validateCategory])
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    createdOn = models.DateField(null=True)

    def __str__(self):
        return self.title
