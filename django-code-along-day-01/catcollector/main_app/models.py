from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.color}"

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


# Create your models here.
class Cat(models.Model):  # IS A
    name = models.CharField(max_length=100)  # HAS A
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    # apple = model.ForeignKey(Basket, on_delete=models.CASCADE)
    # apple_id
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"
