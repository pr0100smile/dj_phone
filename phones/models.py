from django.db import models

# Create your models here.
class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.id};" \
               f" {self.name};" \
               f" {self.price};" \
               f" {self.image};" \
               f" {self.release_date};" \
               f" {self.lte_exists};" \
               f" {self.slug}"