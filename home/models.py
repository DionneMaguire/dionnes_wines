from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))
RATING = [
    (0, '0 stars'),
    (1, '1 stars'),
    (2, '2 stars'),
    (3, '3 stars'),
    (4, '4 stars'),
    (5, '5 stars'),
]


class CustomerReview(models.Model):
    """
    Model for Customer Review
    """
    name = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=0)
    is_customer = models.BooleanField(default=False, null=True, blank=True)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name
