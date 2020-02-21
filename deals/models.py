from django.db import models

class Deal(models.Model):
    stock = models.CharField(max_length=50)
    price_deal = models.DecimalField(max_digits=5, decimal_places=2)
    volume_deal = models.IntegerField()
    sum_deal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date_deal = models.DateField()

    def summary(self):
        self.sum_deal = self.price_deal * self.volume_deal
        self.save()

    def __str__(self):
        return self.stock