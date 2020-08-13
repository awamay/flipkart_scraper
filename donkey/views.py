from django.shortcuts import render
import csv, io
from django.contrib import messages
from .models import Mobile

# Create your views here.
#Name	Storage_details	Screen_size	Camera_details	
#Battery_details	Processor	Warranty	Price in Rupees

#parameter request
def mobile_upload(request):
	#declaring template
	template = "mobile_upload.html"
	data = Mobile.objects.all()


	prompt = {
		'order': 'Order of the CSV should be name, storage_details, screen size, camera details, battery details, processor, warranty, price',
		'mobiles': data,
	}

	if request.method=="GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	#check if its a csv file
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')


	data_set = csv_file.read().decode('UTF-8')


	#setting up a stream
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		created = Mobile.objects.update_or_create(
			Name = column[0],
			Storage_details = column[1],
			Screen_size = column[2],
			Camera_details = column[3],
			Battery_details = column[4],
			Processor = column[5],
			Warranty = column[6],
			Price = column[7]
			)

	context = {}
	return render(request, template, context)

