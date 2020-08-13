from django.db import models

# Create your models here.
#Name	Storage_details	Screen_size	Camera_details	
#Battery_details	Processor	Warranty	Price in Rupees


class Mobile(models.Model):
	Name = models.CharField(max_length=150)
	Storage_details = models.CharField(max_length=150)
	Screen_size = models.CharField(max_length=150)
	Camera_details = models.CharField(max_length=150)
	Battery_details = models.CharField(max_length=150)
	Processor = models.CharField(max_length=150)
	Warranty = models.CharField(max_length=150)
	Price = models.CharField(max_length=150)

	def __str__(self):
		return self.Name

