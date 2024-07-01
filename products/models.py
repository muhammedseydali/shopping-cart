from django.db import models

class Products(models.Model):
    LIVE = 1
    DELETED = 0
    Product_status = ((LIVE,'Live')(DELETED,'Deleted'))
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    description = models.TextField(max_length=200)
    images = models.ImageField(upload_to='/media')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=Product_status, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()