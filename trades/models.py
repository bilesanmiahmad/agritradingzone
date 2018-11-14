from django.db import models
from django.utils.translation import ugettext_lazy as _

from trades import constants as c
from accounts.models import User

# Create your models here.


class Crop(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=30
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name='products'
    )
    quantity = models.DecimalField(
        _('quantity'),
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField(
        _('Image'),
        upload_to='images/',
        blank=True,
        null=True
    )
    details = models.TextField(
        _('details')
    )
    prod_date = models.DateField(
        _('production date'),
        blank=True,
        null=True
    )
    exp_date = models.DateField(
        _('expiry date'),
        blank=True,
        null=True
    )
    price = models.DecimalField(
        _('price'),
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True
    )
    metric = models.CharField(
        _('metric'),
        max_length=5,
        choices=c.METRIC,
        default=c.KILOS
    )
    is_closed = models.BooleanField(
        _('is closed'),
        default=False
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True
    )

    def summary(self):
        return self.details[:50]


class Bid(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='bids'
    )
    client = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='user_bids',
        blank=True,
        null=True
    )
    package = models.CharField(
        _('package'),
        max_length=10,
        choices=c.PACKAGES,
        default=c.BAG
    )
    weight = models.IntegerField(
        _('weight'),
        blank=True,
        null=True
    )
    price = models.DecimalField(
        _('price'),
        max_digits=7,
        decimal_places=2
    )
    is_accepted = models.BooleanField(
        _('is accepted'),
        default=False
    )
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        _('updated'),
        auto_now=True
    )


class Document(models.Model):
    name = models.CharField(
        _('Document name'),
        max_length=50,
        choices=c.DOCUMENTS,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='docs'
    )
    file = models.FilePathField(
        _('Document')
    )
    created = models.DateTimeField(
        _('date created'),
        auto_now_add=True
    )


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profiles'
    )
    address = models.TextField(
        blank=True
    )
    website = models.URLField(
        max_length=300,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    interests = models.ManyToManyField(
        Product,
        related_name='profile_interests'
    )
    created = models.DateTimeField(
        _('date created'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        _('date updated'),
        auto_now=True
    )


