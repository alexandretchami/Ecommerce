from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
    ("Paris & Paris", "Paris & Paris"),
    ("Melun & Melun", "Melun & Melun"),
    ("Versailles & Versailles", "Versailles & Versailles"),
    ("Evry & Evry", "Evry & Evry"),
    ("Nanterre & Nanterre", "Nanterre & Nanterre"),
    ("Bobigny & Bobigny", "Bobigny & Bobigny"),
    ("Créteil & Créteil", "Créteil & Créteil"),
    ("Pontoise & Pontoise", "Pontoise & Pontoise"),
    ("Seine-et-Marne & Seine-et-Marne", "Seine-et-Marne & Seine-et-Marne"),
    ("Essone & Essone", "Essone & Essone"),
    ("Yvelines & Yvelines", "Yvelines & Yvelines"),
    ("Hauts-de-seine & Hauts-de-seine", "Hauts-de-seine & Hauts-de-seine"),
    ("Seine-Saint-Denis & Seine-Saint-Denis", "Seine-Saint-Denis & Seine-Saint-Denis"),
    ("Val-de-Marne & Val-de-Marne", "Val-de-Marne & Val-de-Marne"),
    (
        "Boulogne-Billancourt & Boulogne-Billancourt",
        "Boulogne-Billancourt & Boulogne-Billancourt",
    ),
    ("Montreuil & Montreuil", "Montreuil & Montreuil"),
    ("Courbevoie & Courbevoie", "Courbevoie & Courbevoie"),
    ("Colombes & Colombes", "Colombes & Colombes"),
    ("Vitry-sur-Seine & Vitry-sur-Seine", "Vitry-sur-Seine & Vitry-sur-Seine"),
    ("Argenteuil & Argenteuil", "Argenteuil & Argenteuil"),
    (
        "15e Arrondissement de Paris & 15e Arrondissement de Paris",
        "15e Arrondissement de Paris & 15e Arrondissement de Paris",
    ),
    (
        "14e Arrondissement de Paris & 14e Arrondissement de Paris",
        "14e Arrondissement de Paris & 14e Arrondissement de Paris",
    ),
    (
        "13e Arrondissement de Paris & 13e Arrondissement de Paris",
        "13e Arrondissement de Paris & 13e Arrondissement de Paris",
    ),
    (
        "12e Arrondissement de Paris & 12e Arrondissement de Paris",
        "12e Arrondissement de Paris & 12e Arrondissement de Paris",
    ),
    (
        "11e Arrondissement de Paris & 11e Arrondissement de Paris",
        "11e Arrondissement de Paris & 11e Arrondissement de Paris",
    ),
    (
        "10e Arrondissement de Paris & 10e Arrondissement de Paris",
        "10e Arrondissement de Paris & 10e Arrondissement de Paris",
    ),
    (
        "9e Arrondissement de Paris & 9e Arrondissement de Paris",
        "9e Arrondissement de Paris & 9e Arrondissement de Paris",
    ),
    (
        "8e Arrondissement de Paris & 8e Arrondissement de Paris",
        "8e Arrondissement de Paris & 8e Arrondissement de Paris",
    ),
    (
        "7e Arrondissement de Paris & 7e Arrondissement de Paris",
        "7e Arrondissement de Paris & 7e Arrondissement de Paris",
    ),
    (
        "6e Arrondissement de Paris & 6e Arrondissement de Paris",
        "6e Arrondissement de Paris & 6e Arrondissement de Paris",
    ),
    (
        "11e Arrondissement de Paris & 11e Arrondissement de Paris",
        "11e Arrondissement de Paris & 11e Arrondissement de Paris",
    ),
    (
        "5e Arrondissement de Paris & 5e Arrondissement de Paris",
        "5e Arrondissement de Paris & 5e Arrondissement de Paris",
    ),
    (
        "4e Arrondissement de Paris & 4e Arrondissement de Paris",
        "4e Arrondissement de Paris & 4e Arrondissement de Paris",
    ),
    (
        "3e Arrondissement de Paris & 3e Arrondissement de Paris",
        "3e Arrondissement de Paris & 3e Arrondissement de Paris",
    ),
    (
        "2e Arrondissement de Paris & 2e Arrondissement de Paris",
        "2e Arrondissement de Paris & 2e Arrondissement de Paris",
    ),
    (
        "1e Arrondissement de Paris & 1e Arrondissement de Paris",
        "1e Arrondissement de Paris & 1e Arrondissement de Paris",
    ),
)

CATEGORY_CHOICES = (
    ("jea", "jeans"),
    ("chau", "chaussures"),
    ("jup", "jupes"),
    ("pul", "pulls"),
    ("top", "T-shirts"),
    ("vest", "vestes"),
    ("rob", "robes"),
    ("combi", "combinaisons"),
    ("blaz", "blazers"),
    ("mail", "maillot de bain"),
    ("lun", "lunettes"),
    ("bag", "sacs"),
    ("hat", "chapeaux"),
    ("ceint", "ceintures"),
    ("mech", "meches"),
    ("bc", "Beauté & Cosmétique"),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    product_image = models.ImageField(upload_to="product")

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
