from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Wine(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    grape = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    region = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=80, null=True, blank=True)
    vintage = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class WineReview(models.Model):
    """
    Model for Wine Reviews
    """
    STATUS = ((0, "Draft"), (1, "Published"))
    RATING = [
        (0, '0 stars'),
        (1, '1 stars'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]

    wine = models.ForeignKey(
        Wine, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=0)
    is_customer = models.BooleanField(default=False, null=True, blank=True)
    review = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Reviews ordered to show oldest to newest
        """
        ordering = ['date_created']

    def __str__(self):
        return f"Review {self.review} of {self.wine} by {self.name}"
