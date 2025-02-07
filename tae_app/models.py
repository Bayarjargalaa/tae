from django.db import models



class Product(models.Model):
    PkId = models.AutoField(primary_key=True)  # Auto-generated primary key field if needed
    Id = models.IntegerField()
    Barcode = models.CharField(max_length=255)  # Assuming Barcode is alphanumeric
    Name = models.CharField(max_length=255)
    QtyInPackage = models.IntegerField()  # If QtyInPackage is numeric
    BasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    SalePrice = models.DecimalField(max_digits=10, decimal_places=2)  # Make SalePrice a DecimalField
    ItemGroupId = models.CharField(max_length=255)
    ItemCategoryId = models.CharField(max_length=255)
    ItemCategoryName = models.CharField(max_length=255)
    MeasureName = models.CharField(max_length=255)
    ManufacturerId = models.CharField(max_length=255)
    ManufacturerName = models.CharField(max_length=255)
    ItemSubCategoryId = models.CharField(max_length=255)
    ItemSubCategoryName = models.CharField(max_length=255)
    BrandId = models.CharField(max_length=255)
    BrandName = models.CharField(max_length=255)
    Volume = models.FloatField()  # If Volume is numeric, use FloatField
    Weight = models.FloatField()  # If Weight is numeric, use FloatField
    ActiveStatus = models.BooleanField()  # If ActiveStatus is boolean (True/False)
    name = models.CharField(max_length=255) 
    box_number = models.CharField(max_length=50) 
    size = models.CharField(max_length=50) 
    country = models.CharField(max_length=100) 
    image_url = models.URLField(max_length=200)
    
    
    def __str__(self): 
        return self.name