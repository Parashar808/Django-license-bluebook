from unicodedata import category
from django.db import models





# Create your models here.

class license(models.Model):
    license_number=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='pics')
    blood_group=models.CharField(max_length=3)
    dob=models.CharField(max_length=20)
    father_name=models.CharField(max_length=200)    
    contact_number=models.CharField(max_length=20)
    category=models.CharField(max_length=10)
    issue_date=models.CharField(max_length=10)
    expiry_date=models.CharField(max_length=10)
    issue=models.CharField(max_length=10, default='not-issued')
    
    def __str__(self):
        return self.name

class bluebook(models.Model):
    name=models.CharField(max_length=100, null=True)
    book_number=models.CharField(max_length=100)
    bike_number=models.CharField(max_length=100,null=True)
    photo=models.ImageField(upload_to='pics')
    issue_date=models.CharField(max_length=10)
    expiry_date=models.CharField(max_length=10)
    tax_status=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Nationalid(models.Model):
    
    id_number=models.CharField(max_length=20)
    name=models.CharField(max_length=20, null=True)
    license_number=models.ForeignKey(license, on_delete=models.CASCADE,null=True)
    bluebook_number=models.ForeignKey(bluebook, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
class License_Fine(models.Model):
    Fine_Id = models.CharField(max_length=10)
    amount=models.CharField(max_length=10)
    name= models.OneToOneField(license,on_delete=models.CASCADE )

class Bluebook_Fine(models.Model):
    Fine_Id = models.CharField(max_length=10)   
    amount=models.CharField(max_length=10)
    name= models.OneToOneField(bluebook,on_delete=models.CASCADE )






