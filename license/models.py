from unicodedata import category
from django.db import models





# Create your models here.

class license(models.Model):
    license_number=models.CharField(max_length=20,null='TRUE')
    name=models.CharField(max_length=200,null='TRUE')
    address=models.CharField(max_length=200,null='TRUE')
    citizenship_no=models.CharField(max_length=200,null='TRUE')
    photo=models.ImageField(upload_to='pics',null='TRUE')
    blood_group=models.CharField(max_length=3,null='TRUE')
    dob=models.CharField(max_length=20,null='TRUE')
    father_name=models.CharField(max_length=200,null='TRUE')    
    contact_number=models.CharField(max_length=20,null='TRUE')
    category=models.CharField(max_length=10,null='TRUE')
    issue_date=models.CharField(max_length=10,null='TRUE')
    expiry_date=models.CharField(max_length=10,null='TRUE')

    
    def __str__(self):
        return self.license_number

class bluebook(models.Model):
    v_category=models.CharField(max_length=200, null='TRUE')
    v_model=models.CharField(max_length=200,null='TRUE')
    name=models.CharField(max_length=100,null='TRUE')
    address=models.CharField(max_length=200,null='TRUE')
    book_number=models.CharField(max_length=100,null='TRUE')
    bike_number=models.CharField(max_length=100,null=True)
    photo=models.ImageField(upload_to='pics',null='TRUE')
    issue_date=models.CharField(max_length=10,null='TRUE')
    expiry_date=models.CharField(max_length=10,null='TRUE')
    tax_status=models.CharField(max_length=10,null='TRUE')
    contact_number=models.CharField(max_length=200,null='TRUE')
    manufacture_date=models.CharField(max_length=200,null='TRUE')
    no_of_cylinders=models.CharField(max_length=200,null='TRUE')
    power=models.CharField(max_length=200,null='TRUE')
    chechis_no=models.CharField(max_length=200,null='TRUE')
    engine_no=models.CharField(max_length=200,null='TRUE')
    color=models.CharField(max_length=200,null='TRUE')
    capacity=models.CharField(max_length=200,null='TRUE')
    engine_type=models.CharField(max_length=200,null='TRUE')
    use=models.CharField(max_length=200,null='TRUE')
    permit_for=models.CharField(max_length=200,null='TRUE')
    def __str__(self):
        return self.book_number


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
    national_id= models.OneToOneField(license,on_delete=models.CASCADE )

class Bluebook_Fine(models.Model):
    Fine_Id = models.CharField(max_length=10)   
    amount=models.CharField(max_length=10)
    name= models.OneToOneField(bluebook,on_delete=models.CASCADE )






