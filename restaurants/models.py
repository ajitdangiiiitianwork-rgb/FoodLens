from django.db import models

class Cuisine(models.Model):
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class Restaurant(models.Model):
  name = models.CharField(max_length=200, unique=True)
  address = models.TextField()
  cuisines = models.ManyToManyField(Cuisine, related_name='restaurants')
  rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
  price_range = models.CharField(max_length=50, blank=True)

  def __str__(self):
    return self.name

class MenuItem(models.Model):
  restaurant = models.ForeignKey(
    Restaurant,
    on_delete=models.CASCADE,
    related_name='menu_items'
  )

  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  cuisine = models.ForeignKey(
    Cuisine,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="menu_item"
  )

  is_vegetarian = models.BooleanField(default=False)

  def __str__(self):
    return self.name
