from django.db import models
from config.g_model import BaseModel
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel,BaseModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,)
    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        return self.name
    

class Brand(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category',null=True,blank=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.name